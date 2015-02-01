__author__ = 'basnal'
from Actors.TimeKeeper import TimeKeeper
from Actors.Path import Path
import googlemaps
import pprint


class GMap:
    PickUp = ""
    DropOff = ""
    MapService = googlemaps.Client(key='AIzaSyCb4y2S1BNpcTYtFjV9nd58N2E3etxe-O4')
    pp = pprint.PrettyPrinter(indent=2)
    time = TimeKeeper()
    Rasta = Path()

    def addLocations(self, locA, locB):
        self.PickUp = locA
        self.DropOff = locB

    def findRoute(self, bus):
        self.PickUpGeocode = self.MapService.geocode(self.PickUp)
        self.DropOffGeocode = self.MapService.geocode(self.DropOff)

        #print self.PickUpGeocode[0]['geometry']['location']

        # The directions must be calculated with midways
        print bus.origin
        print bus.destination
        self.directions = self.MapService.directions(bus.origin, bus.destination,
                                                     waypoints=self.getWaypoints(bus),
                                                     mode='driving',
                                                     optimize_waypoints=True)

        # for total time self.directions[0]['legs'][0]['duration']

        self.time.formatToTime(self.TimeDistanceOfTravel(self.directions[0]['legs'])[0])
        self.time.printTime()
        #self.pp.pprint(self.directions[0]['legs'])

        print self.time.TotalMinutes
        print bus.Tmax

        # Main DRT algorithm
        bus.printBus()
        Hubs, bus = self.drtAlgo(bus)

        print "\n\nafter algo"
        bus.printBus()

        return {'locations': {'origin': self.PickUpGeocode,
                              'destination': self.DropOffGeocode},
                'bus': bus}

    def findRouteWithoutBus(self):
        if not self.PickUp or not self.DropOff:
            return

        self.PickUpGeocode = self.MapService.geocode(self.PickUp)
        self.DropOffGeocode = self.MapService.geocode(self.DropOff)

        # The directions must be calculated with midways
        self.directions = self.MapService.directions(self.PickUp, self.DropOff)


        # print self.directions[0]['legs'][0]['steps'][0]
        #for i in self.directions[0]['legs'][0]['steps'][0]:
            #print i

        return {'locations': {'origin': self.PickUpGeocode,
                              'destination': self.DropOffGeocode},
                'directions': self.directions}

    def getWaypoints(self, bus):

        if len(bus.route) > 0:
            waypoints = bus.route
            waypoints.append(self.PickUpGeocode[0]['geometry']['location'])
            waypoints.append(self.DropOffGeocode[0]['geometry']['location'])
            return waypoints

        else:
            return [self.PickUp, self.DropOff]

    def TimeDistanceOfTravel(self, stops):
        result = [0, 0]
        for stop in stops:
            result[0] = result[0] + stop['duration']['value']
            result[1] = result[1] + stop['distance']['value']

        return result

    def drtAlgo(self, bus):
        # Presently this algo only considers Tmax of the bus
        if self.time.TotalMinutes > bus.Tmax:
            Hubs = bus.route
            Hubs.insert(0, bus.origin)
            Hubs.append(bus.destination)
            print 'if'
        else:
            print 'else'
            Hubs = bus.route
            Hubs.insert(0, bus.origin)
            Hubs.append(self.PickUpGeocode[0]['geometry']['location'])
            Hubs.append(self.DropOffGeocode[0]['geometry']['location'])
            bus.route = Hubs
            Hubs.append(bus.destination)
            bus.Duration = self.directions[0]['legs'][0]['duration']['value'] / 60
            bus.Distance = self.directions[0]['legs'][0]['distance']['value'] / 1000

        return Hubs, bus
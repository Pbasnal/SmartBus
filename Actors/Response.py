__author__ = 'basnal'

import pprint
import json

class DRTResponse:
    Status = "Route Found"
    BusName = "Default Bus"
    Origin = {}
    Destination = {}
    Duration = {}
    Distance = {}
    Way = []
    Waypoints = {}
    pp = pprint.PrettyPrinter()

    def responseOfBus(self, bus):
        if bus == None:
            self.Status = "Route not found"
            return

        self.Origin = {'lat': bus.origin[0],
                       'lng': bus.origin[1]}
        self.Destination = {'lat': bus.destination[0],
                            'lng': bus.destination[1]}

        for loc in bus.route:
            self.Way.append({
                'location': {'lat': loc[0],
                             'lng': loc[1]},
                'stopover': True
            })

        print "\n\n>>>Bus route"
        self.Waypoints = {'way': self.Way}#json.dumps(self.Way)
        #self.pp.pprint(self.Way)

        self.Duration = {'time': bus.Duration}
        self.Distance = {'distance': bus.Distance}

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
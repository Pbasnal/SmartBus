__author__ = 'basnal'
# This class app handles the buses during the processing of algorithm.

#from Actors.models import BusModel
from Actors.Bus import Bus
from Actors.Response import DRTResponse

import pprint

# Class Buses maintains the list of buses used during the processing
class Buses:
    BusList = [Bus()]
    AcceptingBusList = []

    pp = pprint.PrettyPrinter()

    drtResponse = DRTResponse()

    def getBus(self, pickup, dropoff):
        # this function returns the most appropriate bus to pick up a customer
        # at origin and going to destination

        # this query needs to be modified to get buses that are near origin
        # and in another phase also consider near destination
        # self.BusList = BusModel.objects.all()
        # for now we use only one bus
        # self.BusList.append()

        NearByBuses = self.nearByBuses(pickup, dropoff)

        for bus in NearByBuses:
            if bus.accept(pickup, dropoff):
                self.AcceptingBusList.append(bus)
                break

        print "The accepting bus list :->\n"
        self.pp.pprint(self.AcceptingBusList)
        print "\n\n\n"

        if self.AcceptingBusList.__len__() != 0:
            self.AcceptingBusList[0].confirm()

            print("\n\nSelected Bus >>\n")
            self.pp.pprint(self.AcceptingBusList[0].route)

            self.drtResponse.responseOfBus(self.AcceptingBusList[0])

        #print "\n\n>>>> response in json"
        #self.pp.pprint(self.drtResponse.to_JSON())


        return self.drtResponse

    def nearByBuses(self, pickup, dropoff):

        nearByBusList = []

        for bus in self.BusList:
            res = bus.getDistanceAndTimeFrom(pickup)
            '''
            print "\n\n\nDistance and time response : \n"
            self.pp.pprint(res['rows'][0]['elements'][0])
            print "\n\n\n"
            '''
            if res != None and res['rows'][0]['elements'][0]['duration']['value'] <= 900:
                nearByBusList.append(bus)
        return nearByBusList






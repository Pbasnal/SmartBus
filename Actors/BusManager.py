__author__ = 'basnal'
# This class app handles the buses during the processing of algorithm.

#from Actors.models import BusModel
from GoogleMapAPI.api import GMap
from operator import attrgetter
from Actors.Bus import Bus


# Class Buses maintains the list of buses used during the processing
class Buses:
    BusList = []
    Gmap = GMap()

    def getBus(self, origin, destination):
        # this function returns the most appropriate bus to pick up a customer
        # at origin and going to destination

        # this query needs to be modified to get buses that are near origin
        # and in another phase also consider near destination
        # self.BusList = BusModel.objects.all()
        # for now we use only one bus
        self.BusList.append(Bus())

        self.Gmap.addLocations(origin, destination)


        TempBus = Bus()
        for bus in self.BusList:
            TempResult = self.Gmap.findRoute(bus)

            #print bus

            if TempBus.Duration == 0 or TempBus.Duration < bus.Duration:
                TempBus = bus
                Result = TempResult

        return Result






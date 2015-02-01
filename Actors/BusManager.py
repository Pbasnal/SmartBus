__author__ = 'basnal'
# This class app handles the buses during the processing of algorithm.

#from Actors.models import BusModel
from Actors.Bus import Bus

# Class Buses maintains the list of buses used during the processing
class Buses:
    BusList = []
    AcceptingBusList = []

    def getBus(self, pickup, dropoff):
        # this function returns the most appropriate bus to pick up a customer
        # at origin and going to destination

        # this query needs to be modified to get buses that are near origin
        # and in another phase also consider near destination
        # self.BusList = BusModel.objects.all()
        # for now we use only one bus
        self.BusList.append(Bus())

        for bus in self.BusList:
            if bus.accept(pickup, dropoff):
                self.AcceptingBusList.append(bus)







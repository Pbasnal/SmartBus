__author__ = 'basnal'

from Actors.Customer import Customer
from GoogleMapAPI.api import GMap

class Bus:
    origin = {'lat': 18.6183, 'lng': 73.8768} # 'army institute of technology, pune'
    destination = {'lat': 18.6183, 'lng': 73.8768} # 'baner, pune'
    route = []#[{'lat': 18.5726, 'lng': 73.8782}, {'lat': 18.5604, 'lng': 73.8360}]    #wadi and bhosari
    NewRoute = []
    Duration = 00
    Distance = 00

    distanceTable = []

    Gmap = GMap()   # Gmap to get routes
    Customers = []  # List of customers in the bus

    def printBus(self):
        print "origin      : %s" % self.origin
        print "destination : %s" % self.destination
        print "route       : %s" % self.route
        print "Tmax        : %d" % self.Tmax
        print "Duration    : %d" % self.Duration
        print "Distance    : %d" % self.Distance

    def addCustomer(self, pickup, dropoff):
        self.NewCustomer = Customer(pickup, dropoff)

    def accept(self, pickup, dropoff):
        self.addCustomer(pickup, dropoff)
        self.createNewRoute()

        self.directions = self.Gmap.findRouteofBus(self)

        self.fillDistanceTable(self.directions[0]['leg'][0['steps']])

        for cust in self.Customers:
            if self.directions[0] > cust.Tmax:
                return False

        return True

    def createNewRoute(self):
        self.NewRoute = self.route
        self.NewRoute.append(self.NewCustomer.pickup())
        self.NewRoute.append(self.NewCustomer.dropoff())

    def fillDistanceTable(self, stops):
        # fill distance table using the stops
        pass









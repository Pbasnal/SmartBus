__author__ = 'basnal'

from Actors.Customer import Customer
from GoogleMapAPI.api import GMap

import pprint
import json


class Bus:
    origin = [18.6183, 73.8768]  # 'army institute of technology, pune'
    destination = [18.6183, 73.8768]  # 'baner, pune'
    route = [[18.6183, 73.8768], [18.6183, 73.8768]]  # [{'lat': 18.5726, 'lng': 73.8782}, {'lat': 18.5604, 'lng': 73.8360}]    #wadi and bhosari
    NewRoute = []
    Duration = 00
    Distance = 00

    pp = pprint.PrettyPrinter()

    TimeTable = []

    Gmap = GMap()  # Gmap to get routes
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

        self.fillTimeTable(self.directions[0]['legs'])

        print "searching for >>> "
        self.pp.pprint(self.NewCustomer.PickUp)

        t1 = [item for item in self.TimeTable if
              round(item["location"]["lat"], 4) == round(self.NewCustomer.PickUp[0], 4)
              and round(item["location"]["lng"], 4) == round(self.NewCustomer.PickUp[1], 4)]
        t2 = [item for item in self.TimeTable if
              round(item["location"]["lat"], 4) == round(self.NewCustomer.DropOff[0], 4)
              and round(item["location"]["lng"], 4) == round(self.NewCustomer.DropOff[1], 4)]

        self.pp.pprint("Pickup loc :")
        self.pp.pprint(t1)
        self.pp.pprint("DropOff loc :")
        self.pp.pprint(t2)
        self.pp.pprint("time diff   :")
        self.pp.pprint(t2[0]["time"] - t1[0]["time"])
        self.pp.pprint("Cust Tmax   :")
        self.pp.pprint(self.NewCustomer.Tmax)

        if t2[0]["time"] - t1[0]["time"] > self.NewCustomer.Tmax:
            return False

        for cust in self.Customers:
            t1 = [item for item in self.TimeTable if round(item["location"]["lat"], 4) == round(cust.PickUp[0], 4)
                  and round(item["location"]["lng"], 4) == round(cust.PickUp[1], 4)]
            t2 = [item for item in self.TimeTable if round(item["location"]["lat"], 4) == round(cust.DropOff[0], 4)
                  and round(item["location"]["lng"], 4) == round(cust.DropOff[1], 4)]

            self.pp.pprint("Pickup loc :")
            self.pp.pprint(t1)
            self.pp.pprint("DropOff loc :")
            self.pp.pprint(t2)
            self.pp.pprint("time diff   :")
            self.pp.pprint(t2[0]["time"] - t1[0]["time"])
            self.pp.pprint("Cust Tmax   :")
            self.pp.pprint(cust.Tmax)

            if t2[0]["time"] - t1[0]["time"] > cust.Tmax:
                return False

        return True

    def createNewRoute(self):
        self.NewRoute = self.route
        self.NewRoute.append(self.NewCustomer.pickup())
        self.NewRoute.append(self.NewCustomer.dropoff())

    def fillTimeTable(self, stops):
        print ">>>> Stops"
        self.TimeTable.append({"location": stops[0]["start_location"], "time": 0})
        for stop in stops:
            self.pp.pprint(stop["distance"])
            # self.pp.pprint(stop['duration'])
            self.TimeTable.append({"location": stop["end_location"],
                                   "time": self.TimeTable[-1]["time"] + stop["duration"]["value"]
            })
            self.pp.pprint(self.TimeTable)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def confirm(self):
        self.route = self.NewRoute
        self.Customers.append(self.NewCustomer)







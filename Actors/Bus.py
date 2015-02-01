__author__ = 'basnal'

class Bus:
    origin = 'army institute of technology, pune'
    destination = 'baner, pune'
    route = []#[{'lat': 18.5726, 'lng': 73.8782}, {'lat': 18.5604, 'lng': 73.8360}]    #wadi and bhosari
    Tmax = 80
    Duration = 35
    Distance = 19

    def printBus(self):
        print "origin      : %s" % self.origin
        print "destination : %s" % self.destination
        print "route       : %s" % self.route
        print "Tmax        : %d" % self.Tmax
        print "Duration    : %d" % self.Duration
        print "Distance    : %d" % self.Distance

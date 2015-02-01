__author__ = 'basnal'

import time
from GoogleMapAPI.api import GMap

class Customer:
    id = 00
    PickUp = []     # lat lng
    DropOff = []    # lat lng
    Tmax = 0
    Distance = 0
    Gmap = GMap()

    def __init__(self):
        self.id = time.time()

    def __init__(self, pickup, dropoff):
        self.id = time.time()
        self.PickUp = self.Gmap.getGeocodeFor(pickup)
        self.DropOff = self.Gmap.getGeocodeFor(dropoff)

        self.setTimenDistance()

    def addLocations(self, pickup, dropoff):
        self.PickUp = self.Gmap.getGeocodeFor(pickup)
        self.DropOff = self.Gmap.getGeocodeFor(dropoff)

        self.setTimenDistance()

    def pickup(self):
        return self.PickUp

    def dropoff(self):
        return self.DropOff

    def setTimenDistance(self):
        stops = self.Gmap.findRoute(self.PickUp, self.DropOff, "transit")

        self.Tmax = 900 + stops['duration']['value']
        self.Distance = stops['distance']['value']

        """
        for stop in stops:
            print stops[stop]
            self.Tmax = self.Tmax + stops[stop]['value']
            self.Distance = self.Distance + stops[stop]['value']
        """
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from GoogleMapAPI.api import GMap
from Actors.BusManager import Buses

import json

Gmap = GMap()
buses = Buses()

def showMap(request):
    args = {'showonlymap': 'true'}
    args.update(csrf(request))
    args['res'] = 'true'
    return render_to_response("map.html", args)

def setPath(request):
    '''
    Gmap.PickUp  = request.POST['origin']
    Gmap.DropOff = request.POST['destination']

    res = Gmap.findRouteWithoutBus()
    '''
    #print "This is what i have got :-> ", request.POST
    res = buses.getBus(request.POST['origin'], request.POST['destination'])
    if res.Status == "Route not found":
        res = None

    args = {}

    if not res:
        args = {'showonlymap': 'true'}
        args.update(csrf(request))
        args['response'] = 'true'
        return render_to_response("map.html", args)

    args['res'] = res.to_JSON()
    args['showonlymap'] = 'false'

    print "\n\nBus route >>> ", res.Waypoints

    return render_to_response("map.html", args)

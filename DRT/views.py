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
    args['bus'] = 'true'
    return render_to_response("map.html", args)

def setPath(request):
    '''
    Gmap.PickUp  = request.POST['origin']
    Gmap.DropOff = request.POST['destination']

    res = Gmap.findRouteWithoutBus()
    '''

    bus = buses.getBus(request.POST['origin'], request.POST['destination'])
    args = {}

    if not bus:
        args = {'showonlymap': 'true'}
        args.update(csrf(request))
        args['response'] = 'true'
        return render_to_response("map.html", args)

    args['bus'] = bus.to_JSON()
    args['showonlymap'] = 'false'

    return render_to_response("map.html", args)

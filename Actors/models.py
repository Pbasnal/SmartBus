from django.db import models

# Bus model to handle bus data

class BusModel(models.Model):
    bus_id = models.CharField(max_length=30)
    route = models.CharField(max_length=30)
    duration = models.TimeField()
    distance = models.DecimalField()
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
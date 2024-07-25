from django.db import models

class Bus(models.Model):
    number_plate = models.CharField(max_length=15, unique=True)
    capacity = models.IntegerField()

class Route(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.FloatField()

class Booking(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

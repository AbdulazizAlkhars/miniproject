from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    organizer = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    image = models.CharField(max_length=250)
    num_of_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

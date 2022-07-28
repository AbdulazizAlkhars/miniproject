from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

"""
The model must have the following fields:
- `organizer`: shouldn't exceed 20 characters and must be unique
- `name`: should not include the word `event`
- `email`: should be a valid email format / can't be empty
- `image`: can't be empty
- `num_of_seats`: can't be less than 5
- `booked_seats`: has a default value of 0 and can't be greater than `num_of_seats`
- `start_date`: should be after today's date
- `end_date`: shouldn't be before `start_date`
"""


class Event(models.Model):
    organizer = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.CharField(max_length=250, blank=True, null=True)
    num_of_seats = models.IntegerField(validators=[MinValueValidator(5)])
    booked_seats = models.IntegerField(
        default=0, validators=[MaxValueValidator(num_of_seats)])
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

from dataclasses import field
from pickle import NONE
from rest_framework import serializers
from .models import Event
import datetime


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


"""
Create a route that receives a query and filters according to the names of the events.
"""
"""
name: should not include the word event
"""
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


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_DateVlaidator(self, data):
        if data['start_date'] < datetime.date.today():
            raise serializers.ValidationError(
                "Event start date should be after today's date")
        return data

    def validate_EndDateValidator(self, data):
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError(
                "Event end date should be after start date")
        return data

    def validate_NameValidator(self, data):
        if 'event' in data['name'].lower():
            raise serializers.ValidationError(
                "Event name should not include the word event")
        return data


class EventsFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


"""
Create a route that fetches a list of fully booked events only.
"""


class EventsFullyBookedSerializer (serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    # def validate_FullyBookedValidator(self, data):
    #     if data['booked_seats'] == data['num_of_seats']:
    #         raise serializers.ValidationError(
    #             "Event is fully booked")
    #     return data

from rest_framework import serializers
from .models import Event


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["organizer", "name", "email", "image",
                  "num_of_seats", "booked_seats", "start_date", "end_date"]


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["organizer", "name", "email", "image",
                  "num_of_seats", "booked_seats", "start_date", "end_date"]

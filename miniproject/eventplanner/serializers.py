from rest_framework import serializers
from .models import Event


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

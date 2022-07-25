from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Event
from .serializers import CreateEventSerializer, EventsListSerializer, EventsUpdateSerializer
# Create your views here.

"""
I want to create a class that Create a route that creates events.
"""


class AddEventAPIView(CreateAPIView):
    serializer_class = CreateEventSerializer


class EventsListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsListSerializer

# Create a route that fetches one event only with all its attributes.


class EventDetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'


class EventObjUpdateView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'


class EventObjDeleteView(DestroyAPIView):
    queryset = Event.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'

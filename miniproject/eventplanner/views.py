from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .models import Event
from .serializers import CreateEventSerializer, EventsListSerializer
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

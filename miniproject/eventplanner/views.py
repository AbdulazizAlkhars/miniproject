from typing import Generic
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from .models import Event
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CreateEventSerializer, EventsListSerializer, EventsUpdateSerializer, EventsFilterSerializer
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


"""
Create a route that receives a query and filters according to the names of the events.
"""


class EventFilterView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsFilterSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        return Event.objects.filter(name__icontains=name)

from typing import Generic
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from .models import Event
from .serializers import CreateEventSerializer, EventsListSerializer, EventsUpdateSerializer, EventsFilterSerializer, EventsFullyBookedSerializer
from rest_framework import filters

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
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = EventsFilterSerializer

    # def get_queryset(self):
    #     return Event.objects.filter(
    #         name_icon__icontains=self.request.query_params.get['name'])


"""
Create a route that fetches a list of fully booked events only.
"""


# class FullyBookedListView(ListAPIView):

#     # queryset = Event.objects.filter(
#     #     booked_seats=int(Event.object.num_of_seats))
#     serializer_class = EventsFullyBookedSerializer

#     def get_queryset(self):
#         fully_booked = Event.objects.filter()
#         return fully_booked

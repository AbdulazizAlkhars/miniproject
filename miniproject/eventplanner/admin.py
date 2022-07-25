from django.contrib import admin
from .models import Event

# Register your models here.

admin.site.register(Event)

"""
Create a route that receives a query and filters according to the names of the events.

"""


# @admin.register(Event)
# class EventFilter(admin.ModelAdmin):
#     title = 'Event Filter'
#     parameter_name = 'event_filter'
#     list_display = ('id', 'name')

#     def lookups(self, request, model_admin):
#         return Event.objects.values_list('name', flat=True).distinct()

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(name__icontains=self.value())
#         return queryset

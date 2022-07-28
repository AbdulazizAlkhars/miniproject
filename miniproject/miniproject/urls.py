"""miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eventplanner import views as event_views

"""
Create a route that fetches a list of fully booked events only.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-event/', event_views.AddEventAPIView.as_view(),
         name="create-event"),
    path('events-list/', event_views.EventsListView.as_view(),),
    path('event-details/<int:event_id>/',
         event_views.EventDetailView.as_view(),),
    path('update-event/<int:event_id>/',
         event_views.EventObjUpdateView.as_view()),
    path('cancel-event/<int:event_id>/',
         event_views.EventObjDeleteView.as_view()),
    path('event-filter/',
         event_views.EventFilterView.as_view()),
    path('fullybooked-list/', event_views.FullyBookedListView.as_view()),
]

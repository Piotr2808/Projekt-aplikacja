from django.urls import include, path
from .views import EventListView, HomeView, EventCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='events'),
    path('events_create/', EventCreateView.as_view(), name='event_create')
]
from django.views.generic import TemplateView, ListView
from .models import Event
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'

class EventListView(ListView):
    template_name = 'event_list.html'
    model = Event

class EventCreateView(CreateView):
    template_name = 'event_create.html'
    model = Event
    fields = ['name', 'description', 'date_from', 'date_to', 'location_name', 'longitude', 'latitude']
    success_url = reverse_lazy('events')

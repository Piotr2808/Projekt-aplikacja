from django.views.generic import TemplateView, ListView
from .models import Event

class HomeView(TemplateView):
    template_name = 'home.html'


class EventListView(ListView):
    template_name = 'event_list.html'
    model = Event
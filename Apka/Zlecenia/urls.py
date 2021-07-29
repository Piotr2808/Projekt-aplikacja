from django.urls import include, path
from .views import EventListView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='events')
]
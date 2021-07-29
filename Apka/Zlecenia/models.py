from django.db import models
from django.contrib import admin

class Event(models.Model):
    name = models.CharField(max_length=80, verbose_name="Event name")
    description = models.TextField(verbose_name="Event description")
    date_from = models.DateField(verbose_name="Event date start")
    date_to = models.DateField(verbose_name="Event date end")
    location_name = models.CharField(max_length=120, blank=True, default="")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Event longitude", null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Event latitude", null=True, blank=True)
    
    def __str__(self):
        return self.name

    @admin.display(description='Event duration [days]')
    def event_duration(self):
        date_duration = (self.date_to - self.date_from).days
        return date_duration


class Employee(models.Model):
    first_name = models.CharField(max_length=80, verbose_name="First Name")
    last_name = models.CharField(max_length=80, verbose_name="Last Name")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class EventEmployee(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)


class EventNote(models.Model):
    mode = models.CharField(max_length=1, choices=(('n', 'Note'), ('a', 'Accident')), default='n')
    description = models.TextField(verbose_name="Note")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
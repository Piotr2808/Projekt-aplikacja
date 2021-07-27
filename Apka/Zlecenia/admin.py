from django.contrib import admin
from .models import Event, Employee, EventEmployee

class EventEmployeeAdmin(admin.TabularInline):
    model = EventEmployee

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    #exclude = ('name', 'date_from')
    list_display = ('name', 'date_from', 'date_to', 'location_name', 'event_duration')
    inlines = [EventEmployeeAdmin,]

admin.site.register(Employee)
from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'aqi', 'timestamp')
    list_filter = ('temperature', 'humidity', 'aqi', 'timestamp')
    search_fields = ('temperature', 'humidity', 'aqi')
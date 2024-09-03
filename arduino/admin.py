from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'aqi', 'ppm', 'ppm')
    list_filter = ('temperature', 'humidity', 'aqi', 'ppm', 'ppm')
    search_fields = ('temperature', 'humidity', 'aqi', 'ppm', 'ppm')


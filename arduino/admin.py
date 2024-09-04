from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'aq', 'ppm')
    list_filter = ('temperature', 'humidity', 'aqi', 'ppm', )
    search_fields = ('temperature', 'humidity', 'aqi', 'ppm',)


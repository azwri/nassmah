from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity' , 'ppm', 'aqi')
    list_filter = ('temperature', 'humidity', 'ppm', 'aqi', )
    search_fields = ('temperature', 'humidity', 'ppm', 'aqi',)


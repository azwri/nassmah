from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp','latitude', 'longitude' ,'temperature', 'humidity' , 'ppm', 'aqi')
    list_filter = ('timestamp','latitude', 'longitude' ,'temperature', 'humidity', 'ppm', 'aqi', )
    search_fields = ('timestamp','latitude', 'longitude' ,'temperature', 'humidity', 'ppm', 'aqi',)


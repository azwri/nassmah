from django.contrib import admin
from .models import SensorData, Device

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'aqi', 'ppm', 'ppm')
    list_filter = ('temperature', 'humidity', 'aqi', 'ppm', 'ppm')
    search_fields = ('temperature', 'humidity', 'aqi', 'ppm', 'ppm')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'device_name', 'device_type')
    list_filter = ('device_id', 'device_name', 'device_type')
    search_fields = ('device_id', 'device_name', 'device_type')
from django.db import models
from django.conf import settings


class Device(models.Model):
    device_id = models.IntegerField(unique=True)
    device_name = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Device {self.device_id}: {self.device_name} ({self.device_type})"


class SensorData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, default='user')
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    aqi = models.CharField(max_length=50)
    ppm = models.FloatField(blank=True, null=True)  # PPM is optional
    latitude = models.FloatField(default=18.2465)  # Default latitude
    longitude = models.FloatField(default=42.5117)  # Default longitude
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Device {self.device_id}: Temp={self.temperature}, Humidity={self.humidity}, AQI={self.aqi}, PPM={self.ppm}, Location=({self.latitude}, {self.longitude}), Timestamp={self.timestamp}"

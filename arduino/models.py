# from django.db import models

# class SensorData(models.Model):
#     temperature = models.FloatField()
#     humidity = models.FloatField()
#     aqi = models.CharField(max_length=50)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Temp: {self.temperature}, Humidity: {self.humidity}, AQI: {self.aqi}"

from django.db import models

class SensorData(models.Model):
    device_id = models.IntegerField(default=0)
    temperature = models.FloatField()
    humidity = models.FloatField()
    aqi = models.CharField(max_length=50)
    ppm = models.FloatField(blank=True, null=True)  # PPM is optional
    latitude = models.FloatField(default=18.2465)  # Default latitude
    longitude = models.FloatField(default=42.5117)  # Default longitude
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Device {self.device_id}: Temp={self.temperature}, Humidity={self.humidity}, AQI={self.aqi}, PPM={self.ppm}, Location=({self.latitude}, {self.longitude}), Timestamp={self.timestamp}"

from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    coordinate = models.CharField(max_length=50)
    temperature = models.CharField(max_length=20)
    pressure = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
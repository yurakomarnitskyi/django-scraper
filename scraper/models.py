from django.db import models


class Car(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price_usd = models.IntegerField(null=True)
    odometer = models.IntegerField()
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    images_count = models.IntegerField(null=True, blank=True)
    car_number = models.CharField(max_length=20, null=True, blank=True)
    car_vin = models.CharField(max_length=50, null=True, blank=True)
    datetime_found = models.DateTimeField(auto_now_add=True)

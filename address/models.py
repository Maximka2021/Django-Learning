from django.db import models


class Address(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)

class Games(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(max_length=5)


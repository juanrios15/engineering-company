from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

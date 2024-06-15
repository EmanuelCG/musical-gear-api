from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
class Category(models.Model):
    category_name = models.CharField(max_length=255, null=False, blank=False, unique=True)

class Country(models.Model):
    country_name = models.CharField(max_length=255, null=False, blank= False, unique=True)

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

class Instrument(models.Model):
    instrument_name = models.CharField(max_length=255, null=False, blank=False)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=False)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    description = models.TextField(null=False, blank=False)

class Item(models.Model):
    instrument_id = models.ForeignKey(Instrument, on_delete=models.SET_NULL, null=True, blank=False)
    serial_number = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    year_of_production = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
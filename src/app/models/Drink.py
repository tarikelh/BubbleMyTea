from django.db import models
from .Crud import Crud

class Drink(models.Model, Crud):
    class Meta:
        db_table = 'app_drink'

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    photo = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=6.00)
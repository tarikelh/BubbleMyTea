from django.db import models
from .Crud import Crud
class Topping(models.Model, Crud):
    class Meta:
        db_table = 'app_topping'

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.50)
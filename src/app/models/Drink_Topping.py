from django.db import models
from .Drink import Drink
from .Topping import Topping
from .Crud import Crud

class Drink_Topping(models.Model, Crud):
    class Meta:
        db_table = 'app_drink_topping'

    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
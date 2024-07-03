from django.db import models
from .Order import Order
from .Drink import Drink
from .Crud import Crud

class Order_Drink(models.Model, Crud):
    class Meta:
        db_table = 'app_order_drink'

    SUGAR_QUANTITY_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    sugar_quantity = models.IntegerField(choices=SUGAR_QUANTITY_CHOICES)

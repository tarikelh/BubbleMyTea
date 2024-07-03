from django.db import models
from .User import User
from .Crud import Crud

class Order(models.Model, Crud):
    class Meta:
        db_table = 'app_order'

    command_date = models.DateField()
    state = models.CharField(max_length=50)
    num_order = models.CharField(max_length=50)
    total_order = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

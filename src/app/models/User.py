from django.db import models
from .Crud import Crud

class User(models.Model, Crud):
    class Meta:
        db_table = 'app_user'

    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
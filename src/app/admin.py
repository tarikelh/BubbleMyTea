from django.contrib import admin

# Register your models here.
#from .models import  User, Topping, Order, Order_Drink, Drink, BubbleTea, BubbleTea_Topping
from .models.User import User
from .models.Topping import Topping
from .models.Order import Order
from .models.Order_Drink import Order_Drink
from .models.Drink import Drink
from .models.Drink_Topping import Drink_Topping

admin.site.register(User)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(Order_Drink)
admin.site.register(Drink)
admin.site.register(Drink_Topping)
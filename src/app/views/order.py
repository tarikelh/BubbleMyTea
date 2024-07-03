import json

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse

from ..models.Order import Order
from ..models.Drink import Drink
from ..models.Topping import Topping


class OrderView(View):
    def get(self, request):
        drink_list = Drink.findAll()
        topping_list = Topping.findAll()
        context = {'drink_list': drink_list, 'topping_list': topping_list}
        return render(request, 'index.html', context)

    def post(self, request):
        try:
            # if not request.session.get('id'): redirect('login')
            print("here")

            data = json.loads(request.body)
            command_date = data.get('command_date')
            state = data.get('state')
            user_id = data.get('user_id')
            total = data.get('total')
            cart = data.get('cart')

            print('there' , total)

            if not all([command_date, state, total, user_id, cart]):
                raise ValueError('Paramètres manquants')

            

            order_id = Order.create_order_with_cart(command_date, state, user_id, total, cart)

            print('anywhere')
            return JsonResponse({ 'message': f'Commande {order_id} ajoutée avec succès'})
        except ValueError as ve:
            return JsonResponse({ 'error': str(ve) })


import json
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.http import JsonResponse

from ..models.Drink import Drink


class AdminView(View):
    def get(self, request):
        drink_list = Drink.findAll()
        context = {'drink_list': drink_list}
        return render(request, 'index.html', context)

    def post(self, request):
        try:
            name = request.POST['name']
            description = request.POST['description']
            photo = request.FILES['photo']
            price = request.POST['price']

            if not all([name, description, photo, price]):
                raise ValueError('Attributs manquants')

            data = {
                'name':name,
                'description':description,
                'photo': '/static/images/drinks/' + photo.name if photo else None,
                'price':price,
            }

            # print("POST", data)
            Drink.create(data)

            return JsonResponse({'message': 'Données reçues avec succès'})
        except ValueError as ve:
            messages.error(request, str(ve))

    def put(self, request, drink_id):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            description = data.get('description')
            photo = data.get('photo')
            price = data.get('price')

            if not all([name, description, photo, price]):
                raise ValueError('Attribut(s) manquant(s)')

            data = {
                'name': name,
                'description': description,
                'photo': '/static/images/drinks/' + photo,
                'price': price,
            }

            # print("PUT", data)

            where = {'id': drink_id }

            Drink.update(data, where)

            return JsonResponse({ 'message': 'Boisson modifiée avec succés' })
        except ValueError as ve:
            messages.error(request, str(ve))
        


    def delete(self, request, drink_id):
        try:
            Drink.destroy({ 'id': drink_id })

            return JsonResponse({ 'message': 'Boisson supprimée avec succès' })
        except ValueError as ve:
            messages.error(request, str(ve))


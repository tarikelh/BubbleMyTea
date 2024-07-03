# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from ..utils.isemail_unique import is_email_unique
from ..models.User import User


# Create your views here.
# @login_required
class ProfileView(View):
    def get(self, request):
        return render(request, 'index.html')

    

    def put(self, request):
        user_id = request.session.get('id')

        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')

        try:
            if not all([lastname, firstname, email]):
                raise ValueError('Attribut(s) manquant(s)')
            
            if not is_email_unique(email, user_id):
                raise ValueError('Adresse email déjà utilisé')

            data = {
                'lastname': lastname,
                'firstname': firstname,
                'email': email
            }

            where = { 'id' : user_id }

            User.update(data, where)

            messages.success(request, 'Profil bien mis à jour')
        except ValueError as ve:
            messages.error(request, str(ve))
        
        return redirect('dashboard')
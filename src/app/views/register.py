from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from ..models.User import User
from ..utils.isvalid import is_valid
from ..utils.bcrypt import Bcrypt

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']

        try:
            if lastname == "" or firstname == "" or email == "" or password == "":
                raise ValueError('missing parameters')

            is_valid_email = is_valid.email(email)
            if is_valid_email is False:
                raise ValueError('invalid email')

            is_valid_password = is_valid.password(password)
            if is_valid_password['val'] is False:
                raise ValueError(is_valid_password['message'])

            user_found = User.findOne({ 'email': email })
            if user_found is True:
                raise ValueError('user already exists')

            hashed_password = Bcrypt.hash_password(password)

            User.create({ 'lastname': lastname, 'firstname': firstname, 'email': email, 'password': hashed_password, 'role': 'user' })

            return redirect('/')
        except ValueError as ve:
            messages.error(request, str(ve))
            return redirect('register')

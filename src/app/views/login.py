from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from ..models.User import User
from ..utils.jwt import Jwt
from ..utils.bcrypt import Bcrypt


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if email == "" or password == "":
                raise ValueError('missing parameters')
            
            user_found = User.findOne({ 'email': email })

            if user_found is None:
                raise ValueError('user not found')

            is_valid_password = Bcrypt.check_password(password, user_found.password)

            if is_valid_password is False:
                raise ValueError('invalid password')
            
            data = {
                'user_id': user_found.id,
                'email': user_found.email,
                'role': user_found.role
            }

            csrf = request.session['csrf']
            token = Jwt.generate_token(data, csrf)

            request.session['token'] = token

            if (user_found.role == 'admin'):
                return redirect('/admin')
            else:
                return redirect('/')
        except ValueError as ve:
            messages.error(request, str(ve))
            return redirect('login')

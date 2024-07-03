from django.shortcuts import render, redirect
from django.views import View

from ..models.Order import Order

# Create your views here.
class DashboardView(View):
    def get(self, request):
        # if not request.session.get('id'): return redirect('login')

        # user_id = request.session.get('id')
        # context = Order.find_orders_with_dependances_by_user({'id': user_id})

        return render(request, 'index.html')

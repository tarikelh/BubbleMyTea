from django.urls import path

from .views.login import LoginView
from .views.register import RegisterView
from .views.dashboard import DashboardView
from .views.profile import ProfileView
from .views.admin import AdminView
from .views.order import OrderView

urlpatterns = [
    path('', OrderView.as_view(), name='order'),

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('me/', ProfileView.as_view(), name='profile'),

    path('admin/', AdminView.as_view(), name='admin'),

    path('admin/<int:drink_id>/', AdminView.as_view(), name='admin'),
    path('admin/<int:drink_id>/', AdminView.as_view(), name='admin'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='mycart'),
    path('history/', views.purchase_history_view, name='purchase_history'),
]

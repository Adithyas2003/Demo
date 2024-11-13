from django.urls import path
from .import views

urlpatterns = [
    path('login',views.e_shop_login),
    path('shop_home',views.shop_home),
]
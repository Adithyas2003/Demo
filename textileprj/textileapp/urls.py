from django.urls import path
from .import views

urlpatterns = [
    path('',views.e_shop_login),
    path('shop_home',views.shop_home),
    path('logout',views.e_shop_logout),
    path('addproduct',views.add_product),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),


    path('register',views.register),
    path('user_home',views.user_home),
]
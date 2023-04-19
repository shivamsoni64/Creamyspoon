from django.urls import path
from app2 import views

urlpatterns = [
                 path('register',views.registeration,name='register'),
                 path('login',views.login,name='login'),
                 path('logout',views.logout,name='logout'),
                 path('cart',views.cart,name='cart'),

]   
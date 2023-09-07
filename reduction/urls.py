from . import  views
from django.urls import path
app_name = 'reduction'


urlpatterns =[

    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('newpage',views.newpage,name='newpage'),
    path('add',views.add,name='add'),
    path('newuser',views.newuser,name='newuser'),





]
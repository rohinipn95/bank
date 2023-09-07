from django.urls import path

from . import views
app_name = 'bank'

urlpatterns = [
    path('add/', views.create_view, name='add'),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX
]
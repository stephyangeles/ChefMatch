from django.urls import path
from . import views

urlpatterns = [
    path('chefs/', views.chef_list, name='chef_list'),
]
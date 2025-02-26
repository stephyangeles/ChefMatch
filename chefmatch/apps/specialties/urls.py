from django.urls import path
from . import views

urlpatterns = [
    path('specialties/', views.specialty_list, name='specialty_list'),
]
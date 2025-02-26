from django.shortcuts import render
from .models import Specialty

def specialty_list(request):
    specialties = Specialty.objects.all()
    return render(request, 'specialty_list.html', {'specialties': specialties})

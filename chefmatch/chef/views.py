# chef/views.py
from django.shortcuts import render

def user_list(request):
    # Lógica para mostrar la lista de usuarios
    return render(request, 'user_list.html')

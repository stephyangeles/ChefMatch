from django.shortcuts import render
from .models import Reservation
from apps.chefs.models import Chef
from django.core.mail import send_mail

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def create_reservation(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        date = request.POST.get('date')
        location = request.POST('location')
        chef_id = request.POST.get('chef_id')

        chef = get_object_or_404(Chef, id=chef_id)
        if chef.is_available(date):
            reservation = Reservation.objects.create(user_id=user_id, date=date, location=location, chef=chef)
            return render(request, 'reservation_confirmed.html', {'reservation': reservation})
        else:
            return render(reques, 'chef_unavailable.html', {'chef':chef})
    else:
        chefs = chef.objects.all()
        return render(request, 'create_reservation.html', {'chefs': chefs})
        
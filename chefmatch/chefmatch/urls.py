from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/reservations/', include('apps.reservations.urls')),
    path('api/chefs/', include('apps.chefs.urls')),
    #path('api/ledger/', include('apps.ledger.urls')),
    path('api/specialties/', include('apps.specialties.urls')),
]
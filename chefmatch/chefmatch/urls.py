from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.reservations.urls')),
    path('api/', include('apps.chefs.urls')),
    #path('api/', include('apps.ledger.urls')),
    path('api/', include('apps.specialties.urls')),
]
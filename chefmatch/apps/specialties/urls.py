from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecialtyViewSet, ChefViewSet, UserViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'specialties', SpecialtyViewSet)
router.register(r'chefs', ChefViewSet)
router.register(r'users', UserViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

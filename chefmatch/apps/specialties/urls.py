from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecialtyViewSet, ChefViewSet

router = DefaultRouter()
router.register(r'specialties', SpecialtyViewSet)
router.register(r'chefs', ChefViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

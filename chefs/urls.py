from .views import ChefViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'chefs', ChefViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneralLedgerViewSet

router = DefaultRouter()
router.register(r'admin', GeneralLedgerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

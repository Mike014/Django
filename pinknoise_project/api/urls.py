# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PinkNoiseViewSet

router = DefaultRouter()
router.register(r'pinknoise', PinkNoiseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShiftWorkViewSet

router = DefaultRouter()


router.register('', ShiftWorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
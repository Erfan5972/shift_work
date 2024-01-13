from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShiftWorkViewSet, ShiftWorksForDriverView, ShiftWorksAsDateView, ShiftWorksAsDateTimeView

router = DefaultRouter()


router.register(r'shift-work', ShiftWorkViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/shifts-driver/', ShiftWorksForDriverView.as_view(), name='shifts-for-driver'),
    path('api/shifts-date/', ShiftWorksAsDateView.as_view(), name='list-shifts-as-date'),
    path('api/shifts-date-time/', ShiftWorksAsDateTimeView.as_view(), name='list-shifts-as-date-time'),
]
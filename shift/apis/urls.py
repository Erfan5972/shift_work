from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShiftWorkViewSet, ShiftWorksForDriverView, ShiftWorksAsDateView, \
    ShiftWorksAsDateTimeView, ShiftWorkAsDateTimeDriverView



router = DefaultRouter()
router.register('', ShiftWorkViewSet)

urlpatterns = [
    path('api/shift-work/', include(router.urls)),
    path('api/shifts-driver/', ShiftWorksForDriverView.as_view(), name='shifts-for-driver'),
    path('api/shifts-driver-as-date/', ShiftWorksAsDateView.as_view(), name='list-shifts-as-date'),
    path('api/shifts-driver-as-date-time/', ShiftWorksAsDateTimeView.as_view(), name='list-shifts-as-date-time'),
    path('api/shifts-driver-as-date-time-driver/', ShiftWorkAsDateTimeDriverView.as_view(),
         name='shift-as-date-time-driver-bool')
]
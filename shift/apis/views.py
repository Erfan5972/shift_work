from rest_framework import viewsets

from shift.models import ShiftWork

from .serializers import ShiftWorkSerializer


class ShiftWorkViewSet(viewsets.ModelViewSet):
    queryset = ShiftWork.objects.all()
    serializer_class = ShiftWorkSerializer
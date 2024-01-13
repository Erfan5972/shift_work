from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from shift.models import ShiftWork

from .serializers import ShiftWorkSerializer, ShiftWorksForDriverSerializer, ShiftWorksAsDateSerializer,\
    ShiftWorksAsDateTimeSerializer


class ShiftWorkViewSet(viewsets.ModelViewSet):
    queryset = ShiftWork.objects.all()
    serializer_class = ShiftWorkSerializer


class ShiftWorksForDriverView(generics.GenericAPIView):
    queryset = ShiftWork.objects.all()
    serializer_class = ShiftWorksForDriverSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)


class ShiftWorksAsDateView(generics.GenericAPIView):
    queryset = ShiftWork.objects.all()
    serializer_class = ShiftWorksAsDateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)


class ShiftWorksAsDateTimeView(generics.GenericAPIView):
    queryset = ShiftWork.objects.all()
    serializer_class = ShiftWorksAsDateTimeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)
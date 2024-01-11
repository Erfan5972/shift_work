from rest_framework import serializers

from shift.models import ShiftWork


class ShiftWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftWork
        fields = '__all__'
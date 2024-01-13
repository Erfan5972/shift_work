from django.core.exceptions import ValidationError
from django.db.models import Q

from rest_framework import serializers

from shift.models import ShiftWork
from driver.models import Driver
from car.models import Car
from group_driver.models import GroupDriver
from group_car.models import GroupCar


class ShiftWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftWork
        fields = '__all__'

    def validate(self, attrs):
        content_type = str(attrs['content_type'])
        if content_type == 'Driver | driver':
            queryset = Driver.objects.filter(id=attrs['object_id'])
            if queryset.exists():
                return attrs
            raise ValidationError("The driver with this id does not exist")
        elif content_type == 'Car | car':
            queryset = Car.objects.filter(id=attrs['object_id'])
            if queryset.exists():
                return attrs
            raise ValidationError("The car with this id does not exist")
        elif content_type == 'Group_Driver | group driver':
            queryset = GroupDriver.objects.filter(id=attrs['object_id'])
            if queryset.exists():
                return attrs
            raise ValidationError("The group_driver with this id does not exist")
        elif content_type == 'Group_Car | group car':
            queryset = GroupCar.objects.filter(id=attrs['object_id'])
            if queryset.exists():
                return attrs
            raise ValidationError("The group_driver with this id does not exist")
        return attrs



class ShiftWorksForDriverSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=4)
    driver = serializers.SerializerMethodField(read_only=True)

    def get_driver(self, obj):
        try:
            queryset = ShiftWork.objects.filter(object_id=obj['id'])
            if queryset.exists():
                serialized_data = ShiftWorkSerializer(queryset, many=True).data
                return serialized_data
            else:
                return "No shifts have been registered for this person"
        except ShiftWork.DoesNotExist:
            return "No shifts have been registered for this person"


class ShiftWorksAsDateSerializer(serializers.Serializer):
    date = serializers.DateField()
    driver = serializers.SerializerMethodField(read_only=True)

    def get_driver(self, obj):
        try:
            date = obj['date']
            queryset = ShiftWork.objects.filter(
                Q(start_shift_date__lte=date,
                  end_shift_date__gte=date) |
                Q(start_shift_date__lte=date,
                  end_shift_date__isnull=True),
                content_type__model='driver'
            )
            if queryset.exists():
                srz_data = ShiftWorkSerializer(queryset, many=True).data
                return srz_data
            return 'nobody has not shift in this date'
        except ShiftWork.DoesNotExist:
            return 'nobody has not shift in this date'


class ShiftWorksAsDateTimeSerializer(serializers.Serializer):
    date = serializers.DateField()
    time = serializers.TimeField()
    driver = serializers.SerializerMethodField(read_only=True)

    def get_driver(self, obj):
        try:
            date = obj['date']
            time = obj['time']
            queryset = ShiftWork.objects.filter(
                Q(start_shift_date__lte=date, start_shift_time__lte=time,
                    end_shift_date__gte=date, end_shift_time__gte=time),
                content_type__model='driver',
            )
            if queryset.exists():
                srz_data = ShiftWorkSerializer(queryset, many=True).data
                return srz_data
            return 'Nobody has a shift at this date and time'
        except ShiftWork.DoesNotExist:
            return 'Nobody has a shift at this date and time'
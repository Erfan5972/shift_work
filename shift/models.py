from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ShiftWork(models.Model):
    TYPE_SHIFT = (
                  ('a', 'day'),
                  ('b', 'week'),
                  ('c', 'month'),
                  )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    start_shift_time = models.TimeField(null=True, blank=True)
    start_shift_date = models.DateField()
    end_shift_time = models.TimeField(null=True, blank=True)
    end_shift_date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPE_SHIFT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.name}//{self.id}'
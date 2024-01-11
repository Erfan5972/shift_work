from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from .models import ShiftWork

admin.site.register(ShiftWork)
admin.site.register(ContentType)
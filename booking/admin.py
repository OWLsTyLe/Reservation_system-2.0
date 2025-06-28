from django.contrib import admin
from django.db import models
# from . import models
from .models import Booking
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

class BookingAdmin(ModelAdmin):
    list_display = ('user', 'room', 'start_date', 'end_date', 'created_at')
    list_filter = ('room', 'start_date', 'end_date')
    search_fields = ('user__username', 'room__hotel__name')


admin.site.register(Booking, BookingAdmin)

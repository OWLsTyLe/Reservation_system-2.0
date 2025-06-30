from django.contrib import admin
from django.db import models
from .models import Restaurant, Table, Reservation
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

@admin.register(Restaurant)
class RestaurantAdmin(ModelAdmin):
    list_display = ('name', 'rating', 'image')
    search_fields = ('description',)

    formfield_overrides = {
        models.TextField: {'widget':WysiwygWidget}
    }

@admin.register(Table)
class TableAdmin(ModelAdmin):
    list_display = ("number", "restaurant", "seats")
    list_filter = ("restaurant",)

@admin.register(Reservation)
class ReservationAdmin(ModelAdmin):
    list_display = ("user", "table", "date", "time")
    list_filter = ("date", "table__restaurant")
    search_fields = ("user__username", "table__restaurant__name")

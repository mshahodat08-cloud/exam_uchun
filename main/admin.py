from django.contrib import admin
from .models import Talaba, Guruh


@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('familiya', 'ism')
    search_fields = ('familiya', 'ism')
    ordering = ('familiya', 'ism')


@admin.register(Guruh)
class GuruhAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'tavsif', 'yaratilgan')
    search_fields = ('nomi',)
    ordering = ('-yaratilgan',)

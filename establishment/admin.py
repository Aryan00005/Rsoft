from django.contrib import admin
from .models import EstablishmentBasic

@admin.register(EstablishmentBasic)

class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'state','type')
    search_fields = ('name', 'state','type')

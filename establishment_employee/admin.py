from django.contrib import admin
from .models import EstablishmentEmployee

@admin.register(EstablishmentEmployee)
class EstablishmentEmployeeAdmin(admin.ModelAdmin):
    list_display = ("establishment", "employee", "date_assigned")
    search_fields = ("establishment__name", "employee__user__username")
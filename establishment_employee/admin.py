from django.contrib import admin
from .models import EstablishmentEmployee

@admin.register(EstablishmentEmployee)
class EstablishmentEmployeeAdmin(admin.ModelAdmin):
    list_display = ('get_employee_name', 'get_establishment_name', 'date_joined')
    search_fields = ('employee__name_as_per_aadhar', 'establishment__name')
    list_filter = ('establishment',)

    def get_employee_name(self, obj):
        return obj.employee.name_as_per_aadhar  
    get_employee_name.short_description = 'Employee Name' 

    def get_establishment_name(self, obj):
        return obj.establishment.name  
    get_establishment_name.short_description = 'Establishment Name'  
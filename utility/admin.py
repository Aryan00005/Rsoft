from django.contrib import admin
from .models import Gender, Nationality, Bank, Education, EmploymentType, Designation, ProofOfIdentification, FamilyRelations

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    
@admin.register(EmploymentType)
class EmploymentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    
@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    
@admin.register(ProofOfIdentification)
class ProofOfIdentificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    
@admin.register(FamilyRelations)
class FamilyRelationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    

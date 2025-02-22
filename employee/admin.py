from django.contrib import admin
from django.utils.html import format_html
from .models import EmployeeBasic, EmployeeBankInformation, EmployeeAddress, EmployeePersonalData, EmployeeEmployment, EmployeeFamilyDetail, EmployeeDocument

@admin.register(EmployeeBasic)
class EmployeeBasicAdmin(admin.ModelAdmin):
    list_display = ('name_as_per_aadhar', 'employee_first_name', 'employee_middle_name', 'employee_last_name', 'father_name', 'gender', 'nationality', 'date_of_joining', 'last_increment_date', 'maternity_benefit_date', 'handicap_status', 'employment_status', 'designation', 'department', 'subdepartment', 'staff_worker', 'mobile_number')

@admin.register(EmployeeBankInformation)
class EmployeeBankInformationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'bank', 'account_number', 'branch', 'ifsc', 'pan_card', 'uan_number', 'esic')

@admin.register(EmployeeAddress)
class EmployeeAddressAdmin(admin.ModelAdmin):
    list_display = ('employee', 'current_address', 'permanent_address', 'created', 'updated')

@admin.register(EmployeePersonalData)
class EmployeePersonalDataAdmin(admin.ModelAdmin):
    list_display = ('employee', 'display_photo', 'display_signature', 'anniversary_date', 'hobbies', 'skills', 'proof_of_identification')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
        return "No Photo"

    def display_signature(self, obj):
        if obj.signature:
            return format_html('<img src="{}" width="50" height="50" />', obj.signature.url)
        return "No Signature"


@admin.register(EmployeeEmployment)
class EmployeeEmploymentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'company_name', 'start_date', 'end_date_display', 'created', 'updated')

@admin.register(EmployeeFamilyDetail)
class EmployeeFamilyDetailAdmin(admin.ModelAdmin):
    list_display = ('employee', 'relation', 'name', 'date_of_birth', 'aadhar_number', 'created', 'updated')

@admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'document_type', 'document_number', 'display_document_image', 'created', 'updated')

    def display_document_image(self, obj):
        if obj.document_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.document_image.url)
        return "No Image"

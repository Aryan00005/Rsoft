from django.contrib import admin
from django.utils.html import format_html
from .models import EmployeeBasic, EmployeeBankInformation, EmployeeAddress, EmployeePersonalData, EmployeeEmployment, EmployeeFamilyDetail, EmployeeDocument

@admin.register(EmployeeBasic)
class EmployeeBasicAdmin(admin.ModelAdmin):
    list_display = ('user', 'name_as_per_aadhar_card','first_name', 'middle_name', 'last_name' , 'gender', 'nationality', 'date_of_joining', 'date_of_leaving', 'last_increment_date', 'maternity_benefit_date', 'reason_of_leaving', 'handicap_status', 'employment_status', 'designation', 'department', 'subdepartment', 'staff_worker', 'mobile_number')

@admin.register(EmployeeBankInformation)
class EmployeeBankInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank', 'account_number', 'branch', 'ifsc', 'pan_card', 'uan_number', 'esic')

@admin.register(EmployeeAddress)
class EmployeeAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_address', 'permanent_address', 'created', 'updated')

@admin.register(EmployeePersonalData)
class UserPersonalDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_photo', 'display_signature', 'anniversary_date', 'hobbies', 'skills', 'proof_of_identification')

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
    display_photo.short_description = 'Photo'

    def display_signature(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.signature.url)
    display_signature.short_description = 'Signature'

@admin.register(EmployeeEmployment)
class UserEmploymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'start_date', 'end_date_display', 'created', 'updated')

@admin.register(EmployeeFamilyDetail)
class UserFamilyDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'relation', 'name', 'date_of_birth', 'aadhar_number', 'created', 'updated')

@admin.register(EmployeeDocument)
class UserDocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'document_type', 'document_number', 'display_document_image', 'created', 'updated')

    def display_document_image(self, obj):
        if obj.document_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.document_image.url)
        return "No Image"
    display_document_image.short_description = 'Document Image'
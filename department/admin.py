from django.contrib import admin
from .models import Department, SubDepartment

class SubDepartmentInline(admin.TabularInline):
    model = SubDepartment
    extra = 1

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    inlines = [SubDepartmentInline]

@admin.register(SubDepartment)
class SubDepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "created_at")
    list_filter = ("department",)
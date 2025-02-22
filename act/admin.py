from django.contrib import admin
from .models import Act

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','form_name', 'created_at')
    search_fields = ('name',)

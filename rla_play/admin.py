# rla_play/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("RLA Pay Admin")
admin.site.site_title = _("RLA Pay Admin Portal")
admin.site.index_title = _("Welcome to RLA Pay Admin")
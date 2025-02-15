# filepath: user/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/user-information/', include('user.admin_urls')),
]
# filepath: user/admin_urls.py
from django.urls import path
from .admin_views import user_list_view, user_information_view

urlpatterns = [
    path('', user_list_view, name='user-list'),
    path('<int:user_id>/', user_information_view, name='user-information'),
]
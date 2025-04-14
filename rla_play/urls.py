"""
URL configuration for rla_play project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from home.views import homepage_view
from user_role.views import RegisterView , LoginView , DasboardAdminView , DasboardEstablishmentView , DasboardEmployeeView , SuperadminCreateView , SuperadminUpdateDestroyView , EstablishmentEmployeeCreateView , EstablishmentEmployeeRetrieveUpdateDestroyView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('', homepage_view, name='homepage'),  # Add this line
    path('admin/user/user-information/', include('user.admin_urls')),  # Include the custom admin URLs first
    path('admin/', admin.site.urls),  # Default admin URLs

#dashboard
    path('api/auth/register',RegisterView.as_view(), name= 'auth_register'),
    path('api/auth/login',LoginView.as_view(), name= 'auth_login'),
    path('api/dashboard/admin', DasboardAdminView.as_view(),name = 'admin dashboard'),
    path('api/dashboard/establishment', DasboardEstablishmentView.as_view(),name = 'establishment dashboard'),
    path('api/dashboard/employee', DasboardEmployeeView.as_view(),name = 'employee dashboard'),

#superadmin CRUD
    path('superadmin/user', SuperadminCreateView.as_view(), name = 'Superadmin-create'),
    path('superadmin/user/<int:pk>', SuperadminUpdateDestroyView.as_view(), name = 'Superadmin-detail'),

#Establishment CRUD
    path('establishment/employees', EstablishmentEmployeeCreateView.as_view()),
    path("establishment/employees/<int:pk>", EstablishmentEmployeeRetrieveUpdateDestroyView.as_view()),


#API token & refresh
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
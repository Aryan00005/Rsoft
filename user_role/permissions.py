from rest_framework.permissions import BasePermission


class AdminRole(BasePermission):
    def has_permission(self , request ,view):
            return request.user.user_role.filter(role__name='Admin').exists()
          

class EstablishmentRole(BasePermission):
    def has_permission(self , request ,view):
            return request.user.user_role.filter(role__name='Establishment').exists() or AdminRole().has_permission(request , view)
    

class EmployeeRole(BasePermission):
    def has_permission(self , request ,view):
            return request.user.user_role.filter(role__name='Employee').exists() or EstablishmentRole().has_permission(request , view)
          


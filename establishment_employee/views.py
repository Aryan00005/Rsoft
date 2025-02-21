from rest_framework import viewsets
from .models import EstablishmentEmployee


class EstablishmentEmployeeViewSet(viewsets.ModelViewSet):
    queryset = EstablishmentEmployee.objects.all()
    

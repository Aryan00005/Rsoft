from django.db import models
from establishment.models import Establishment
from employee.models import EmployeeBasic

class EstablishmentEmployee(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name="employees")
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE, related_name="establishment")
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name_as_per_aadhar} - {self.establishment.name}"

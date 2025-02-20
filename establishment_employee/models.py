from django.db import models
from establishment.models import EstablishmentBasic
from employee.models import EmployeeBasic

class EstablishmentEmployee(models.Model):
    establishment = models.ForeignKey(
        EstablishmentBasic, 
        on_delete=models.CASCADE, 
        related_name="employees",
        verbose_name="Establishment"
    )
    employee = models.ForeignKey(
        EmployeeBasic, 
        on_delete=models.CASCADE, 
        related_name="establishments",
        verbose_name="Employee"
    )
    date_assigned = models.DateField(auto_now_add=True, verbose_name="Date Assigned")

    def __str__(self):
        return f"{self.employee.user.username} - {self.establishment.name}"

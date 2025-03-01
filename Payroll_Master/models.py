from django.db import models
from employee.models import EmployeeBasic

class WagesMaster(models.Model):
    name_as_per_record = models.ForeignKey(
        EmployeeBasic, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        verbose_name="Name_as_per_record"
    )
    
    Basic = models.CharField(max_length=20, blank=True, null=True, verbose_name="Basic")
    DA = models.CharField(max_length=20, blank=True, null=True, verbose_name="DA")
    Medical_Allowance = models.CharField(max_length=20, blank=True, null=True, verbose_name="Medical Allowance")
    HRA = models.CharField(max_length=20, blank=True, null=True, verbose_name="HRA")
    Conv_All = models.CharField(max_length=20, blank=True, null=True, verbose_name="Conveyance Allowance")
    Extra_All = models.CharField(max_length=20, blank=True, null=True, verbose_name="Extra Allowances")
    Field_All = models.CharField(max_length=20, blank=True, null=True, verbose_name="Field Allowances")
    Edu_All = models.CharField(max_length=20, blank=True, null=True, verbose_name="Education Allowances")
    LTA = models.CharField(max_length=20, blank=True, null=True, verbose_name="LTA")
    Efficiency_All = models.CharField(max_length=20, blank=True, null=True, verbose_name="Efficiency Allowances")
    Salary_Arrears = models.CharField(max_length=20, blank=True, null=True, verbose_name="Salary Arrears")
    Other_All = models.CharField(max_length=20, blank=True, null=True, verbose_name="Other Allowances")

    def __str__(self):
        return str(self.name_as_per_record) if self.name_as_per_record else "No Name"
    
class DeductionMaster(models.Model):
    name_as_per_record = models.ForeignKey(
        EmployeeBasic, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        verbose_name="Name_as_per_record"
    )
   
    pf = models.CharField(max_length=20, blank=True, null=True, verbose_name="PF")
    pf_no = models.CharField(max_length=20, blank=True, null=True, verbose_name="PF NO.")
    esic = models.CharField(max_length=20, blank=True, null=True, verbose_name="ESIC")
    esic_no = models.CharField(max_length=20, blank=True, null=True, verbose_name="ESIC No.")
    fpf = models.CharField(max_length=20, blank=True, null=True, verbose_name="FPF")
    pension = models.CharField(max_length=20, blank=True, null=True, verbose_name="pension")
    pt = models.CharField(max_length=20, blank=True, null=True, verbose_name="PT")
    tds = models.CharField(max_length=20, blank=True, null=True, verbose_name="TDS")

    def __str__(self):
        return str(self.name_as_per_record) if self.name_as_per_record else "No Name"
    
class EmployeeLiabilityMaster(models.Model):
    name_as_per_record = models.ForeignKey(
        EmployeeBasic, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        verbose_name="Name_as_per_record"
    )
    statutory = models.CharField(max_length=20, blank=True, null=True, verbose_name="Statutory")
    non_statutory= models.CharField(max_length=20, blank=True, null=True, verbose_name="non")
    

    def __str__(self):
        return str(self.name_as_per_record) if self.name_as_per_record else "No Name"

from django.contrib import admin
from .models import WagesMaster, DeductionMaster, EmployeeLiabilityMaster

@admin.register(WagesMaster)
class WagesMasterAdmin(admin.ModelAdmin):
    list_display = ['name_as_per_record','Basic','DA','Medical_Allowance','HRA','Conv_All','Extra_All','Field_All','Edu_All','LTA','Efficiency_All','Salary_Arrears','Other_All']

@admin.register(DeductionMaster)
class DeductionMasterAdmin(admin.ModelAdmin):
    list_display = ['name_as_per_record','pf','pf_no','esic','esic_no','fpf','pension','pt','tds']

@admin.register(EmployeeLiabilityMaster)
class EmployeeLiabilityMasterAdmin(admin.ModelAdmin):
    list_display = ['name_as_per_record','statutory','non_statutory']

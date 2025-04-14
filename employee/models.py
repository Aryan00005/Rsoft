from django.db import models
from django.db import models
from django.contrib.auth.models import User
from utility.models import Gender, Nationality, EmploymentType, Designation, Bank, ProofOfIdentification, FamilyRelations
from department.models import Department, SubDepartment
from .constants import YES_NO_CHOICES, STAFF_WORKER_CHOICES
from .helpers import user_directory_path


class EmployeeBasic(models.Model):
    name_as_per_aadhar = models.CharField(max_length=255, verbose_name="Name as per Aadhar")
    employee_first_name = models.CharField(max_length=30, verbose_name="Employee First Name")
    employee_middle_name = models.CharField(max_length=30, verbose_name="Employee Middle Name")
    employee_last_name = models.CharField(max_length=30, verbose_name="Employee Last Name")
    father_name = models.CharField(max_length=30, verbose_name="Father's Name")
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, verbose_name="Gender")
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True, verbose_name="Nationality")
    date_of_joining = models.DateField(verbose_name="Date of Joining")
    last_increment_date = models.DateField(null=True, blank=True, verbose_name="Last Increment Date")
    maternity_benefit_date = models.DateField(null=True, blank=True, verbose_name="Maternity Benefit Date")
    handicap_status = models.IntegerField(choices=YES_NO_CHOICES, default=0, verbose_name="Handicap Status")
    employment_status = models.ForeignKey(EmploymentType, on_delete=models.SET_NULL, null=True, verbose_name="Employment Status")
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, verbose_name="Designation")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employee_department", verbose_name="Department")
    subdepartment = models.ForeignKey(SubDepartment, on_delete=models.SET_NULL, null=True, related_name="employee_subdepartment", verbose_name="Subdepartment")
    staff_worker = models.CharField(max_length=10, choices=STAFF_WORKER_CHOICES, default='Staff', verbose_name="Staff/Worker")
    mobile_number = models.CharField(max_length=15, verbose_name="Mobile Number")

    def __str__(self):
        return self.name_as_per_aadhar.username


class EmployeeBankInformation(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE, verbose_name="Employee")
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, verbose_name="Bank Name")
    account_number = models.CharField(max_length=30, verbose_name="Account Number")
    branch = models.CharField(max_length=50, verbose_name="Branch")
    ifsc = models.CharField(max_length=11, verbose_name="IFSC")
    pan_card = models.CharField(max_length=10, verbose_name="PAN Card")
    uan_number = models.CharField(max_length=12, verbose_name="UAN Number")
    esic = models.CharField(max_length=17, verbose_name="ESIC")

    def __str__(self):
        return f"{self.employee.username} - {self.bank.name}"

    
class EmployeeAddress(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE, verbose_name="Employee")
    current_address = models.TextField(verbose_name="Current Address")
    permanent_address = models.TextField(verbose_name="Permanent Address")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return f"{self.employee.username} - Address"

    
class EmployeePersonalData(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE, verbose_name="Employee")
    photo = models.ImageField(upload_to=user_directory_path, max_length=1048576, verbose_name="Photo")
    signature = models.ImageField(upload_to=user_directory_path, max_length=1048576, verbose_name="Signature")
    anniversary_date = models.DateField(null=True, blank=True, verbose_name="Anniversary Date")
    hobbies = models.CharField(max_length=255, null=True, blank=True, verbose_name="Hobbies")
    skills = models.CharField(max_length=255, null=True, blank=True, verbose_name="Skills")
    proof_of_identification = models.ForeignKey(ProofOfIdentification, on_delete=models.SET_NULL, null=True, verbose_name="Proof of Identification")

    def __str__(self):
        return f"{self.employee.username} - Personal Data"

    
class EmployeeEmployment(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE, verbose_name="Employee")
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return f"{self.employee.username} - {self.company_name}"


    def end_date_display(self):
        return self.end_date if self.end_date else "Present"
    end_date_display.short_description = 'End Date'
    
class EmployeeFamilyDetail(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE, verbose_name="Employee")
    relation = models.ForeignKey(FamilyRelations, on_delete=models.CASCADE, verbose_name="Relation")
    name = models.CharField(max_length=255, verbose_name="Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    aadhar_number = models.CharField(max_length=12, verbose_name="Aadhar Number")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return f"{self.employee.username} - {self.relation} - {self.name}"

    
class EmployeeDocument(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE, verbose_name="Employee")
    document_type = models.ForeignKey(ProofOfIdentification, on_delete=models.CASCADE, verbose_name="Document Type")
    document_number = models.CharField(max_length=255, verbose_name="Document Number")
    document_image = models.ImageField(upload_to=user_directory_path, max_length=1048576, verbose_name="Document Image")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return f"{self.employee.username} - {self.document_type} - {self.document_number}"

    

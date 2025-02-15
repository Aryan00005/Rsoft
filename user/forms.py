from django import forms
from django.contrib.auth.models import User
from .models import UserBasic, UserBankInformation, UserAddress, UserPersonalData, UserEmployment, UserFamilyDetail, UserDocument

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
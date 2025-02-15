from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserBasic, UserBankInformation, UserAddress, UserPersonalData, UserEmployment, UserFamilyDetail, UserDocument
from .forms import UserInformationForm

def user_list_view(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'admin/user_list.html', context)

def user_information_view(request, user_id):
    user = User.objects.get(pk=user_id)
    user_basic = UserBasic.objects.get(user=user)
    user_bank_info = UserBankInformation.objects.filter(user=user)
    user_address = UserAddress.objects.get(user=user)
    user_personal_data = UserPersonalData.objects.get(user=user)
    user_employment = UserEmployment.objects.filter(user=user)
    user_family_details = UserFamilyDetail.objects.filter(user=user)
    user_documents = UserDocument.objects.filter(user=user)

    if request.method == 'POST':
        form = UserInformationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin:user-information', user_id=user_id)
    else:
        form = UserInformationForm(instance=user)

    context = {
        'user': user,
        'user_basic': user_basic,
        'user_bank_info': user_bank_info,
        'user_address': user_address,
        'user_personal_data': user_personal_data,
        'user_employment': user_employment,
        'user_family_details': user_family_details,
        'user_documents': user_documents,
        'form': form,
    }
    return render(request, 'admin/user_information.html', context)

urlpatterns = [
    path('', user_list_view, name='user-list'),
    path('<int:user_id>/', user_information_view, name='user-information'),
]
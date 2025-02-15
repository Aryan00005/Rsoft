# filepath: user/admin_views.py
from django.shortcuts import render, get_object_or_404, redirect
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
    user = get_object_or_404(User, pk=user_id)
    user_basic = get_object_or_404(UserBasic, user=user)
    user_bank_info = UserBankInformation.objects.filter(user=user)
    user_address = get_object_or_404(UserAddress, user=user)
    user_personal_data = get_object_or_404(UserPersonalData, user=user)
    user_employment = UserEmployment.objects.filter(user=user)
    user_family_details = UserFamilyDetail.objects.filter(user=user)
    user_documents = UserDocument.objects.filter(user=user)

    if request.method == 'POST':
        form = UserInformationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-information', user_id=user_id)
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
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from .models import UserBasic, UserBankInformation, UserAddress, UserPersonalData, UserEmployment, UserFamilyDetail, UserDocument
from .forms import UserInformationForm

class UserInformationAdminView(admin.ModelAdmin):
    change_list_template = "admin/user_list.html"
    list_display = ('username', 'email', 'view_information_button')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:user_id>/', self.admin_site.admin_view(self.user_information_view), name='user-information'),
            path('', self.admin_site.admin_view(self.user_list_view), name='user-list'),
        ]
        return custom_urls + urls

    def user_list_view(self, request):
        users = User.objects.all()
        context = {
            'users': users,
        }
        return render(request, 'admin/user_list.html', context)

    def user_information_view(self, request, user_id):
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

    def view_information_button(self, obj):
        return format_html('<a class="button" href="{}">View Information</a>', reverse('admin:user-information', args=[obj.pk]))
    view_information_button.short_description = 'User Information'
    view_information_button.allow_tags = True

# Register the custom admin view
admin.site.register(User, UserInformationAdminView)
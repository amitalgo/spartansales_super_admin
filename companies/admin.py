from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.db.models import Q

from .models import Companies, CompaniesUsers


class CompanyInline(admin.TabularInline):
    model = CompaniesUsers
    fk_name = 'user'
    can_delete = False

    exclude = ['is_admin']


class CustomUserAdmin(UserAdmin):
    inlines = [
        CompanyInline
    ]
    model = User

    list_display = ['username','email','first_name','last_name','get_company',]

    def get_company(self,obj):
        return obj.companiesusers.company.company_name
    get_company.short_description = 'Company'

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    #
    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         instance.created_by = request.user
    #         instance.save()
    #     formset.save_m2m()

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        return qs.filter(companiesusers__is_admin=1)
        # return qs.filter(~Q(password=''),is_superuser=True)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)

# Register your models here.
admin.site.register(Companies)

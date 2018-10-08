from django.contrib import admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country','created_by',)

    def country(self, obj):
        return obj.country_name

    list_filter = ('country_name', 'status', )

    exclude = ['status','created_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
            instance.save()
        form.save_m2m()

admin.site.register(Country,CountryAdmin)

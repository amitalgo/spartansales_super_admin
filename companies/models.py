from django.db import models
from  django.contrib.auth.models import User

User.add_to_class('is_superadmin',models.IntegerField(default=0))

# Create your models here.
class Companies(models.Model):
    # user = models.OneToOneField(User,blank=False,null=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    company_address = models.CharField(max_length=250)
    company_email = models.CharField(blank=True,null=True,max_length=250)
    def __str__(self):
        return self.company_name

class CompaniesUsers(models.Model):
    user = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Companies, blank=False, null=True, on_delete=models.CASCADE)
    is_admin = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

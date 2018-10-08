from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=250)
    status = models.IntegerField(default=1, help_text='Active/Inactive', choices=((1, 'Active'), (0, 'Inactive'),))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = "Country"

from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    phone_number_additional = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)


class DeliveryAddress(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, blank=False)
    street = models.CharField(max_length=300, null=False, blank=False)
    departament = models.CharField(max_length=100, null=False, blank=False)
    zip_code = models.CharField(max_length=100, null=False, blank=False)
    detail = models.CharField(max_length=300, null=True, blank=True)
    is_active = models.BooleanField(default=True)

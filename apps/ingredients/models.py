from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    is_topping = models.BooleanField(default=False)  # this ingredient can be a topping
    cost = models.FloatField(default=0.0)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

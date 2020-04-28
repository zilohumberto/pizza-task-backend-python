from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    # TODO implement S3
    photo = models.ImageField(verbose_name="photo", width_field=500, height_field=500, null=True, blank=True)


class PricePizza(models.Model):
    pizza = models.ForeignKey(Pizza, null=False, blank=False, on_delete=models.CASCADE)
    size = models.ForeignKey('sizes.Size', null=False, blank=False, on_delete=models.CASCADE)
    price = models.FloatField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

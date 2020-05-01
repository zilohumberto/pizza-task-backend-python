from django.db import models
from base.stores import PizzaModelStorage


class Pizza(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    photo = models.ImageField(
        verbose_name="photo", null=True, blank=True,
        storage=PizzaModelStorage(),
        upload_to=PizzaModelStorage.pizza_photo_path,
    )


class PricePizza(models.Model):
    pizza = models.ForeignKey(Pizza, null=False, blank=False, on_delete=models.CASCADE, related_name="prices")
    size = models.ForeignKey('sizes.Size', null=False, blank=False, on_delete=models.CASCADE)
    price = models.FloatField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

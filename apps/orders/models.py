from django.db import models
from users.models import User


class OrderStatus(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)


class Order(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.status_id:
            self.status_id = OrderStatus.objects.get(name='created').pk
        super(Order, self).save(*args, **kwargs)

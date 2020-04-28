from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PizzaModelStorage(S3Boto3Storage):
    def __init__(self):
        super().__init__(bucket=settings.PIZZA_MODEL_BUCKET)

    @staticmethod
    def pizza_photo_path(instance, filename=None):
        return "{pk}/last_thumbnail.jpg".format(
            pk=instance.pk,
        )

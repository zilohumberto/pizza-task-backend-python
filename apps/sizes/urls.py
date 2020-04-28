from django.conf.urls import url
from rest_framework import routers

from sizes.views import SizeView

router = routers.SimpleRouter()

router.register(r'', SizeView)
urlpatterns = [
]

urlpatterns += router.urls

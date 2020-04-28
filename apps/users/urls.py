from django.conf.urls import url
from rest_framework import routers
from users.views import ContactView, DeliveryAddressView

router = routers.SimpleRouter()

router.register(r'contact/?', ContactView)
router.register(r'delivery_address/?', DeliveryAddressView)
urlpatterns = [
]

urlpatterns += router.urls

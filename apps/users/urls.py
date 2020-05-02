from django.conf.urls import url
from rest_framework import routers
from users.views import ContactView, DeliveryAddressView, UserView

router = routers.SimpleRouter()

router.register(r'contact/?', ContactView)
router.register(r'delivery_address/?', DeliveryAddressView)
router.register(r'user/?', UserView, basename="user")
urlpatterns = [
]

urlpatterns += router.urls

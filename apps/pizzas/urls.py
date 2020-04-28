from django.conf.urls import url
from rest_framework import routers
from pizzas.views import PizzaView, PricePizzaView

router = routers.SimpleRouter()

router.register(r'pizza', PizzaView)
router.register(r'price_pizza', PricePizzaView)
urlpatterns = [
]

urlpatterns += router.urls

from django.conf.urls import url
from rest_framework import routers
from orders.views import OrderStatusView, OrderView

router = routers.SimpleRouter()

router.register(r'order', OrderView, basename="order")
router.register(r'status', OrderStatusView)
urlpatterns = [
]

urlpatterns += router.urls

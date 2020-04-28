from rest_framework.viewsets import ModelViewSet
from base.views import ModelViewSetNSerializer
from rest_framework.permissions import IsAuthenticated
from orders.models import OrderStatus, Order
from orders.serializers import OrderStatusSerializer, OrderSerializer, OrderRestSerializer


class OrderStatusView(ModelViewSet):
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post',)


class OrderView(ModelViewSetNSerializer):
    serializer_class = OrderSerializer
    rest_serializer_class = OrderRestSerializer
    queryset = Order.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post',)

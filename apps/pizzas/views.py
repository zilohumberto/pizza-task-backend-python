from rest_framework.viewsets import ModelViewSet
from base.views import ModelViewSetNSerializer
from rest_framework.permissions import IsAuthenticated
from pizzas.models import Pizza, PricePizza
from pizzas.serializers import PizzaSerializer, PricePizzaSerializer, PricePizzaRestSerializer


class PizzaView(ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete',)


class PricePizzaView(ModelViewSetNSerializer):
    serializer_class = PricePizzaSerializer
    rest_serializer_class = PricePizzaRestSerializer
    queryset = PricePizza.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post',)

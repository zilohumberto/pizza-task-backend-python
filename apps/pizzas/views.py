from base.views import ModelViewSetNSerializer
from rest_framework.permissions import IsAuthenticated
from pizzas.models import Pizza, PricePizza
from pizzas.serializers import PizzaSerializer, PricePizzaSerializer, PricePizzaRestSerializer, PizzaRestSerializer


class PizzaView(ModelViewSetNSerializer):
    serializer_class = PizzaSerializer
    rest_serializer_class = PizzaRestSerializer
    queryset = Pizza.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete', 'options', )


class PricePizzaView(ModelViewSetNSerializer):
    serializer_class = PricePizzaSerializer
    rest_serializer_class = PricePizzaRestSerializer
    queryset = PricePizza.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post',)

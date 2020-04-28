from rest_framework import serializers
from pizzas.models import Pizza, PricePizza
from sizes.serializers import SizeSerializer


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = '__all__'


class PricePizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePizza
        fields = '__all__'


class PricePizzaRestSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(read_only=True)
    size = SizeSerializer(read_only=True)

    class Meta:
        model = PricePizza
        fields = '__all__'

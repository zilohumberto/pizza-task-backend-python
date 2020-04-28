from rest_framework import serializers
from commands.models import CommandStatus, Command, IngredientByClient
from ingredients.serializers import IngredientSerializer
from pizzas.serializers import PricePizzaSerializer


class CommandStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommandStatus
        fields = '__all__'


class IngredientByClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientByClient
        fields = '__all__'


class IngredientByClientRestSerializer(serializers.ModelSerializer):
    ingredient_topping = IngredientSerializer()

    class Meta:
        model = IngredientByClient
        fields = '__all__'


class CommandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Command
        fields = '__all__'


class CommandRestSerializer(serializers.ModelSerializer):
    pizza_ordered = PricePizzaSerializer()
    status = CommandStatusSerializer()
    ingredientbyclient_set = IngredientByClientSerializer(many=True)

    class Meta:
        model = Command
        fields = ('order', 'pizza_ordered', 'status', 'ingredientbyclient_set', 'creation_date', 'update_date',)

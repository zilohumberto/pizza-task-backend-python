from rest_framework import serializers
from commands.models import CommandStatus, Command, IngredientByClient
from ingredients.serializers import IngredientSerializer
from pizzas.serializers import PricePizzaRestSerializer


class CommandStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommandStatus
        fields = '__all__'


class IngredientByClientSerializer(serializers.ModelSerializer):
    ingredient_topping = IngredientSerializer()
    class Meta:
        model = IngredientByClient
        fields = ('id', 'ingredient_topping', 'amount', 'description')


class IngredientByClientRestSerializer(serializers.ModelSerializer):
    ingredient_topping = IngredientSerializer()

    class Meta:
        model = IngredientByClient
        fields = '__all__'


class CommandSerializer(serializers.ModelSerializer):
    toppings = IngredientByClientSerializer(many=True)

    class Meta:
        model = Command
        fields = ('id', 'pizza_ordered', 'order', 'creation_date', 'update_date', 'toppings', 'status', 'amount', )

    def create(self, validated_data):
        """
            Django does not support a relation insertion
        """
        ingredients_validated_data = validated_data.pop('toppings') if 'toppings' in validated_data else []
        command = Command.objects.create(**validated_data)
        ingredients_serializer = self.fields['toppings']
        for each in ingredients_validated_data:
            each['command'] = command
        ingredients_serializer.create(ingredients_validated_data)
        return command


class CommandRestSerializer(serializers.ModelSerializer):
    pizza_ordered = PricePizzaRestSerializer()
    status = CommandStatusSerializer()
    toppings = IngredientByClientSerializer(many=True)

    class Meta:
        model = Command
        fields = ('id', 'order', 'pizza_ordered', 'status', 'toppings', 'creation_date', 'update_date', 'amount', )

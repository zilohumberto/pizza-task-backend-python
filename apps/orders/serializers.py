from rest_framework import serializers
from orders.models import OrderStatus, Order
from users.serializers import UserSerializer, ContactSerializer, DeliveryAddress
from commands.serializers import CommandRestSerializer


class OrderStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('user', 'id', 'status', 'creation_date', 'update_date',  'contact', 'address')


class OrderRestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    command_set = CommandRestSerializer(many=True)
    status = OrderStatusSerializer()
    contact = ContactSerializer()
    address = DeliveryAddress()

    class Meta:
        model = Order
        fields = ('id', 'user', 'command_set', 'status', 'creation_date', 'update_date', 'contact', 'address')

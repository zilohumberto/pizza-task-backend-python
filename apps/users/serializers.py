from rest_framework import serializers
from users.models import Contact, DeliveryAddress, User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = '__all__'


class UserRestSerializer(serializers.ModelSerializer):
    contact = serializers.SerializerMethodField('get_contacts')
    delivery_address = serializers.SerializerMethodField('get_delivery_address')

    @staticmethod
    def get_contacts(user):
        qs = Contact.objects.filter(is_active=True, user=user)
        serializer = ContactSerializer(instance=qs, many=True)
        return serializer.data

    @staticmethod
    def get_delivery_address(user):
        qs = DeliveryAddress.objects.filter(is_active=True, user=user)
        serializer = DeliveryAddressSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'contact', 'delivery_address', 'is_active',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_active', 'password')

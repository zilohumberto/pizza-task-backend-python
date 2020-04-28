from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.models import Contact, DeliveryAddress
from users.serializers import ContactSerializer, DeliveryAddressSerializer


class ContactView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete', )


class DeliveryAddressView(ModelViewSet):
    serializer_class = DeliveryAddressSerializer
    queryset = DeliveryAddress.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete',)

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.models import Contact
from users.serializers import ContactSerializer


class ContactView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete', )

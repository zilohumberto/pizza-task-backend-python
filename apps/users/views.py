from django.db import transaction
from django.http.response import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from base.views import ModelViewSetNSerializer
from users.models import Contact, DeliveryAddress, User
from users.serializers import ContactSerializer, DeliveryAddressSerializer, UserSerializer, UserRestSerializer


class ContactView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete', 'options', )


class DeliveryAddressView(ModelViewSet):
    serializer_class = DeliveryAddressSerializer
    queryset = DeliveryAddress.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete', 'options', )


class UserView(ModelViewSetNSerializer):
    serializer_class = UserSerializer
    rest_serializer_class = UserRestSerializer
    queryset = None
    http_method_names = ('get', 'patch', 'post', 'options', )

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return []
        return [self.request.user]

    def partial_update(self, request, *args, **kwargs):
        if request.user.pk != int(kwargs['pk'].encode('utf-8')):
            return JsonResponse('PRECONDITION_FAILED', status=status.HTTP_412_PRECONDITION_FAILED, safe=False)
        return super(UserView, self).partial_update(request, *args, **kwargs)

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=False)
            precondition = User.objects.filter(username=data['username'])
            if precondition:
                return JsonResponse({"data": 'pre condition failed'}, status=status.HTTP_412_PRECONDITION_FAILED)
            response = super(UserView, self).create(request, *args, **kwargs)
            if response.status_code != 201:
                return response
            user_instance = User.objects.get(username=data['username'])
            user_instance.set_password(data['password'])
            user_instance.save()
            return response
        except Exception as e:
            transaction.set_rollback(True)
            return HttpResponse(str(e), status=status.HTTP_404_NOT_FOUND)

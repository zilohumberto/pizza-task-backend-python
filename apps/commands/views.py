from rest_framework.viewsets import ModelViewSet
from base.views import ModelViewSetNSerializer
from rest_framework.permissions import IsAuthenticated
from commands.models import CommandStatus, Command, IngredientByClient
from commands.serializers import (
    CommandStatusSerializer,
    CommandSerializer,
    IngredientByClientSerializer,
    CommandRestSerializer,
    IngredientByClientRestSerializer,
)


class CommandStatusView(ModelViewSet):
    serializer_class = CommandStatusSerializer
    queryset = CommandStatus.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'options', )


class CommandView(ModelViewSetNSerializer):
    serializer_class = CommandSerializer
    rest_serializer_class = CommandRestSerializer
    queryset = Command.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'options', 'delete', )


class IngredientByClientView(ModelViewSetNSerializer):
    serializer_class = IngredientByClientSerializer
    rest_serializer_class = IngredientByClientRestSerializer
    queryset = IngredientByClient.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete', 'options', )

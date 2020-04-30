from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from sizes.models import Size
from sizes.serializers import SizeSerializer


class SizeView(ModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete', 'options', )

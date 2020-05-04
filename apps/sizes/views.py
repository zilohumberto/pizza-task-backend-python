from rest_framework.viewsets import ModelViewSet
from sizes.models import Size
from sizes.serializers import SizeSerializer


class SizeView(ModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()
    http_method_names = ('get', 'patch', 'post', 'options', )

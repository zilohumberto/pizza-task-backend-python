from rest_framework.viewsets import ModelViewSet


class ModelViewSetNSerializer(ModelViewSet):
    serializer_class = None
    rest_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.rest_serializer_class
        return self.serializer_class

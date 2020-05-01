from rest_framework.viewsets import ModelViewSet


class ModelViewSetNSerializer(ModelViewSet):
    serializer_class = None
    rest_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.rest_serializer_class
        return self.serializer_class

    def get_queryset(self):
        model = self.serializer_class.Meta.model
        if model._meta.pk.name in self.request.GET:
            pk = model._meta.pk.name
            queryset = model.objects.filter(
                **{pk: self.request.GET[pk]}
            )
        else:
            queryset = model.objects.all()
        return queryset

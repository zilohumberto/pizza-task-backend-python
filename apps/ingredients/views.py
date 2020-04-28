from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer


class IngredientView(ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'delete', )

from rest_framework.viewsets import ModelViewSet
from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer


class IngredientView(ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    http_method_names = ('get', 'patch', 'post', 'options', )

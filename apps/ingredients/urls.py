from django.conf.urls import url
from rest_framework import routers

from ingredients.views import IngredientView

router = routers.SimpleRouter()

router.register(r'', IngredientView)
urlpatterns = [
]

urlpatterns += router.urls

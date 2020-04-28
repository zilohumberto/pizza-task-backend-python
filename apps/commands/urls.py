from django.conf.urls import url
from rest_framework import routers
from commands.views import CommandStatusView, CommandView, IngredientByClientView

router = routers.SimpleRouter()

router.register(r'command', CommandView)
router.register(r'status', CommandStatusView)
router.register(r'ingredients_by_client', IngredientByClientView)
urlpatterns = [
]

urlpatterns += router.urls

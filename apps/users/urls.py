from django.conf.urls import url
from rest_framework import routers
from users.views import ContactView

router = routers.SimpleRouter()

router.register(r'contact/?', ContactView)
urlpatterns = [
]

urlpatterns += router.urls

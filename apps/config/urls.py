from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ingredients/', include("ingredients.urls")),
    url(r'^sizes/', include("sizes.urls")),
    url(r'^users/', include("users.urls")),
    url(r'^commands/', include("commands.urls")),
    url(r'^orders/', include("orders.urls")),
    url(r'^pizzas/', include("pizzas.urls")),
]

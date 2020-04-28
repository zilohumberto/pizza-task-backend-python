from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ingredients/', include("ingredients.urls")),
    url(r'^sizes/', include("sizes.urls")),
    url(r'^users/', include("users.urls")),
]

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("multiplayer/", include("channels_demo.urls")),
    path("admin/", admin.site.urls),
]

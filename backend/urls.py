"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .api.views import index_view
from .product.urls import urlpatterns as product_urlpatterns
from .user.urls import urlpatterns as user_urlpatterns

router = routers.DefaultRouter()

urlpatterns = [
    # http://localhost:8000/
    path("", index_view, name="index"),
    # http://localhost:8000/api/admin/
    path("api/admin/", admin.site.urls),
]

urlpatterns.extend(user_urlpatterns)
urlpatterns.extend(product_urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

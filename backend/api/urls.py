from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
from .views import index_view

urlpatterns_base = [path("", index_view, name="index")]
urlpatterns = [path("", include(router.urls))]

from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register("category", CategoryViewSet)
router.register("product", ProductViewSet)
urlpatterns = [
    path("api/", include(router.urls)),
]

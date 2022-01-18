from django.urls import include, path
from rest_framework import routers

from .views import CartProductViewSet, CartViewSet, CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register("category", CategoryViewSet)
router.register("product", ProductViewSet)
router.register("cart", CartViewSet)
router.register("cart-product", CartProductViewSet)
urlpatterns = [
    path("api/", include(router.urls)),
]

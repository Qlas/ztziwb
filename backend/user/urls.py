from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, logout_view

router = routers.DefaultRouter()

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/logout/", logout_view, name="logout_view"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

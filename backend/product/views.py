from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from ..utils.product import get_all_products
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        show_main = request.query_params.get("show_main", "true")
        if show_main == "true":
            queryset = queryset.filter(is_main=True)
            print(queryset, flush=True)
        serializer = self.get_serializer(
            queryset,
            many=True,
        )
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        search = request.query_params.get("search", None)
        if search:
            category = Category.objects.get(name=search)
            data = get_all_products(category)
        else:
            data = self.get_queryset()
        serializer = self.get_serializer(
            data,
            many=True,
        )
        return Response(serializer.data)

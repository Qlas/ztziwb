from nis import cat

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..utils.product import get_all_products
from .models import Cart, CartProduct, Category, Product
from .serializers import CartProductSerializer, CartSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        show_main = request.query_params.get("show_main", "true")
        if show_main == "true":
            queryset = queryset.filter(is_main=True)
        serializer = self.get_serializer(
            queryset,
            many=True,
        )
        return Response(serializer.data)

    def create(self, request):
        if Category.objects.filter(name=request.data["name"]).exists():
            return Response({"nazwa": ["ta nazwa już istnieje"]}, status=400)
        if request.data.get("parent_category", False):
            request.data["parent_category"] = Category.objects.get(name=request.data["parent_category"]).id

        return super().create(request)


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


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by("id")
    serializer_class = CartSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(user=request.user).filter(status__in=("open", "payment"))
        serializer = self.get_serializer(
            queryset,
            many=True,
        )
        return Response(serializer.data)

    @action(methods=["patch"], detail=True)
    def remove_item(self, request, pk=None):
        product = self.get_object().cart_product.filter(product__name=request.data["product"]).first()
        product.delete()
        return Response()

    @action(methods=["patch"], detail=True)
    def change_product_quantity(self, request, pk=None):
        product = self.get_object().cart_product.filter(product__name=request.data["product"]).first()
        if product and product.product.quantity < product.quantity + request.data["quantity"]:
            return Response(status=500)
        product.quantity = request.data["quantity"]
        product.save()
        return Response()

    @action(methods=["patch"], detail=True)
    def end_cart(self, request, pk=None):
        cart = self.get_object()
        cart.status = "end"
        cart.save()
        return Response()


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all().order_by("id")
    serializer_class = CartProductSerializer

    def create(self, request):
        cart = request.user.carts.filter(user=request.user).filter(status__in=("open", "payment")).first()
        if not cart:
            cart = Cart.objects.create(user=request.user)
        request.data["cart"] = cart.id

        product = cart.cart_product.filter(product__name=request.data["product"]).first()
        if product and product.product.quantity < product.quantity + request.data["quantity"]:
            return Response(status=500)
        if product:
            product.quantity += request.data["quantity"]
            product.save()
            return Response()

        return super().create(request)

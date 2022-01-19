from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True)
    is_main = models.BooleanField(default=False)
    parent_category = models.ForeignKey(
        "self", null=True, blank=True, related_name="sub_category", on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=2000, blank=True)
    image = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Cart(models.Model):
    STATUS_CHOICES = [
        ("done", "done"),
        ("payment", "payment"),
        ("open", "open"),
    ]
    user = models.ForeignKey(User, related_name="carts", on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default="open",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.cart.user} - {self.cart.status} - {self.product.name} - {self.quantity}"

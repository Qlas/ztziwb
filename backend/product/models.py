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
    description = models.CharField(max_length=512, blank=True)
    image = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

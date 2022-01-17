from nis import cat

from rest_framework import serializers

from .models import Category, Product


def get_product_count(category):
    products_count = 0
    products_count += category.products.count()
    for sub_category in category.sub_category.all():
        products_count += get_product_count(sub_category)
    return products_count


class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Category
        fields = "__all__"

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        if not self.context.get("request") or self.context.get("request").method != "POST":
            fields["sub_category"] = CategorySerializer(many=True)
        return fields

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["products_count"] = get_product_count(instance)
        return data


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = "__all__"

from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields["sub_category"] = CategorySerializer(many=True)
        return fields


class ProductSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Product
        fields = "__all__"

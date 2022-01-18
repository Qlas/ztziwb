from nis import cat

from rest_framework import serializers

from .models import Cart, CartProduct, Category, Product


def get_product_count(category):
    products_count = 0
    products_count += category.products.count()
    for sub_category in category.sub_category.all():
        products_count += get_product_count(sub_category)
    return products_count


class CategorySerializer(serializers.ModelSerializer):
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


class CartProductSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field="name", queryset=Product.objects.all())
    price = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    max_quantity = serializers.SerializerMethodField()

    def get_price(self, instance):
        return instance.product.price

    def get_image(self, instance):
        return instance.product.image

    def get_max_quantity(self, instance):
        return instance.product.quantity

    class Meta:
        model = CartProduct
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    cart_product = CartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"

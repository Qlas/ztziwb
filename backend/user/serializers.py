from django.contrib.auth.models import Permission, User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import ContactForm


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_permissions = serializers.SlugRelatedField(many=True, read_only=True, slug_field="codename")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "is_staff",
            "is_superuser",
            "user_permissions",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation["is_superuser"]:
            representation["user_permissions"].extend(Permission.objects.all().values_list("codename", flat=True))
        else:
            for group in User.objects.get(username=representation["username"]).groups.all():
                representation["user_permissions"].extend(group.permissions.values_list("codename", flat=True))

        return representation


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["user"] = UserSerializer(user).data

        return token


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"

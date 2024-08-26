from rest_framework import serializers

from account.models import User


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token


class UserSignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password", "confirm_password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        confirm_password = attrs.pop("confirm_password")
        password = attrs.get("password")
        if password != confirm_password:
            raise serializers.ValidationError(
                "Password and Confirm Password Don't Match"
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

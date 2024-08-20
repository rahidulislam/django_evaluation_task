from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user_account.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token["email"] = user.email

        return token
    
    def validate(self, attrs):
        token_data = super().validate(attrs)
        data = {
            "id": self.user.id,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email,
            "access": token_data["access"],
            "refresh": token_data["refresh"],
        }

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user


    def to_representation(self, instance):
        data = super().to_representation(instance)
        refresh = MyTokenObtainPairSerializer.get_token(instance)
        access = refresh.access_token
        data["access"] = str(access)
        data["refresh"] = str(refresh)
        return data

from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Candidate, Recruiter


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("email", "name", "role", "password")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        if user.role == "CANDIDATE":
            Candidate.objects.create(user=user)
        elif user.role == "RECRUITER":
            Recruiter.objects.create(user=user, company_name="")

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            email=data["email"],
            password=data["password"]
        )
        if not user:
            raise AuthenticationFailed("Invalid email or password")
        return user

class ResetSerializer(serializers.Serializer):
    old_password=serializers.CharField(write_only=True)
    new_password=serializers.CharField(write_only=True,min_length=8)
    confirm_password=serializers.CharField(write_only=True)

    def validate(self,data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"password and confirm pasword is not same"}
            )
        return data


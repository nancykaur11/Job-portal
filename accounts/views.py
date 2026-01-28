from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "User registered successfully",
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })






# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework import status
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken

# from .models import User, Candidate, Recruiter


# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         email = request.data.get("email")
#         name = request.data.get("name")
#         role = request.data.get("role")
#         password = request.data.get("password")

#         if not all([email, name, role, password]):
#             return Response(
#                 {"error": "All fields are required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         if User.objects.filter(email=email).exists():
#             return Response(
#                 {"error": "Email already exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         user = User.objects.create_user(
#             email=email,
#             name=name,
#             role=role
#         )
#         user.set_password(password)
#         user.save()

#         if role == "CANDIDATE":
#             Candidate.objects.create(user=user)
#         elif role == "RECRUITER":
#             Recruiter.objects.create(user=user, company_name="")

#         refresh = RefreshToken.for_user(user)

#         return Response({
#             "message": "User registered successfully",
#             "access": str(refresh.access_token),
#             "refresh": str(refresh)
#         }, status=status.HTTP_201_CREATED)


# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         if not email or not password:
#             return Response(
#                 {"error": "Email and password required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         user = authenticate(email=email, password=password)

#         if not user:
#             return Response(
#                 {"error": "Invalid credentials"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         refresh = RefreshToken.for_user(user)

#         return Response({
#             "access": str(refresh.access_token),
#             "refresh": str(refresh)
#         })

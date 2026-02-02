from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Resume

from .serializers import RegisterSerializer, LoginSerializer,ResetSerializer,ResumeUploadSerializer


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

class ResetView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=ResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(serializer.validated_data["old_password"]):
            return Response(
                {"error": "Old password is incorrect"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(serializer.validated_data["new_password"])
        user.save()

        return Response(
            {"message": "Password changed successfully"},
            status=status.HTTP_200_OK
        )
class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResumeUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        candidate = request.user.candidate
        pdf_file = serializer.validated_data["file"]

        resume = Resume.objects.create(
            user=candidate,
            file=pdf_file
        )

        return Response(
            {"message": "Resume uploaded successfully"},
            status=status.HTTP_200_OK
        )



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework import status
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import User, Candidate, Recruiter


# class RegisterView(APIView):
# #     permission_classes=[AllowAny]
    
# #     def post(self,request):
# #         email=request.data.get("email")
# #         name=request.data.get("name")
# #         role=request.data.get("role")
# #         password=request.data.get("password")

# #         if not all([email,name,role,password]):
# #             return Response(
# #                 "All fields are required",
# #                 status=status.HTTP_400_BAD_REQUEST
# #             )
# #         if User.objects.filter(email=email).exists():
# #             return Response(
# #                 "Email already exists",
# #                 status=status.HTTP_400_BAD_REQUEST
# #             )   
            
# #         user=User.objects.create_user(
# #             email=email,
# #             name=name,
# #             role=role
# #         )     
# #         user.set_password(password)
# #         user.save()
        
# #         if role=="CANDIDATE":
# #             Candidate.objects.create(user=user)     
# #         elif role=="RECRUITER":
# #             Recruiter.objects.create(user=user,company_name="")
# #         refresh=RefreshToken.for_user(user)
# #         return Response({
# #             "message":"User registered successfully",
# #             "access":str(refresh.access_token),
# #             "refresh":str(refresh)
# #         },status=status.HTTP_201_CREATED) 


# # class LoginView(APIView):
# #     permission_classes = [AllowAny]
# #     def post(self,request):
# #         email=request.data.get("email")
# #         password=request.data.get("password")
        
# #         if not email or not password:
# #             return Response(
# #                 "Email and password required",
# #                 status= status.HTTP_400_BAD_REQUEST
# #             )
# #         user = authenticate(email=email, password=password)
# #         if not user:
# #             return Response(
# #                 "wrong crendiatal",
# #                 status= status.HTTP_401_UNAUTHORIZED
# #             )
        
# #         refresh = RefreshToken.for_user(user)

# #         return Response({
# #             "access": str(refresh.access_token),
# #             "refresh": str(refresh)
# #         })         
        
        

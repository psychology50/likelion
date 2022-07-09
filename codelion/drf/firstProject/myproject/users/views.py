from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import (
    UserSerializer,
    RegisterUserSerializer,
    ChangePasswordSerializer,
    RefreshTokenSerializer,
)

class CustomUserCreate(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            # create token
            # token = TokenObtainPairSerializer.get_token(newuser)
            # refresh_token = str(token)
            # access_token = str(token.access_token)

            response = Response(
                {
                    "user": reg_serializer.data,
                    "message": "register success",
                    # "token": {
                    #     "access": access_token,
                    #     "refresh": refresh_token,
                    # },
                },
                status=status.HTTP_201_CREATED,
            )

            # response.set_cookie("access", access_token, httponly=True)
            # response.set_cookie("refresh", refresh_token, httponly=True)
            if newuser:
                return response
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CustomUserCreate(APIView):
#     permission_classes = [ AllowAny ]

#     def post(self, request):
#         reg_serializer = RegisterUserSerializer(data=request.data)
#         if reg_serializer.is_valid():
#             newuser = reg_serializer.save()
#             if newuser:
#                 return Response(status=status.HTTP_201_CREATED)
#         return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [ IsAuthenticated ]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'message': 'Password updated successfully',
            }
            return Response(response, status=status.HTTP_200_OK,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ObtainUserTokenView(TokenObtainPairView):
#     permission_classes = [ AllowAny ]
#     serializer_class = ObtainUserTokenSerializer

class CustomUserLogin(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        user = authenticate(
            email = request.data.get("email"),
            password = request.data.get("password"),
        )
        if user:
            login_serializer = UserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            response = Response(
                {
                    "user": login_serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return response
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CustomUserLogout(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request, *args):
        user = RefreshTokenSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response(
                {
                   "message": "logout success" 
                }, status=status.HTTP_204_NO_CONTENT)
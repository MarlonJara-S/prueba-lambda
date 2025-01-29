from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView as SimpleJWTTokenRefreshView
from .models import User
from .serializers import UserCreateSerializer, UserLoginSerializer, UserSerializer

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Usuario registrado con éxito"})

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.validated_data['email']).first()

        if not user:
            return Response({"error": "Credenciales incorrectas"}, status=400)

        if not user.is_active:
            return Response({"error": "Usuario inactivo"}, status=400)

        if not user.check_password(serializer.validated_data['password']): 
            return Response({"error": "Credenciales incorrectas"}, status=400)

        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'id': user.id,
                'email': user.email,
                'role': user.role,
                'username': user.username
            }
        })


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'admin':
            return Response({"error": "No autorizado"}, status=403)

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserEditView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response({"error": "Usuario no encontrado"}, status=404)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        if request.user.role != 'admin':
            return Response({"error": "No autorizado"}, status=403)

        if request.user.id == pk:
            return Response({"error": "No puedes editarte a ti mismo"}, status=400)

        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response({"error": "Usuario no encontrado"}, status=404)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserDesactivateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        if request.user.role != 'admin':
            return Response({"error": "No autorizado"}, status=403)

        if request.user.id == pk:
            return Response({"error": "No puedes desactivarte a ti mismo"}, status=400)

        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response({"error": "Usuario no encontrado"}, status=404)

        user.is_active = False
        user.save()
        return Response({"message": "Usuario desactivado con éxito"})

class TokenRefreshView(SimpleJWTTokenRefreshView):
    pass

from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth.models import User 
from .serializers import RegisterSerializer , LoginSerializer , UserSerializer , SuperadminUserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .permissions import AdminRole , EstablishmentRole , EmployeeRole



class SuperadminCreateView(generics.ListCreateAPIView):
    serializer_class = SuperadminUserSerializer
    permission_classes = [IsAuthenticated, AdminRole]

    def get_queryset(self):
        return User.objects.filter(user_role__role__name__in=["Establishment", "Employee","Contractor"])
    
class SuperadminUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SuperadminUserSerializer
    permission_classes = [IsAuthenticated,AdminRole]

    def get_queryset(self):
        return User.objects.filter(user_role__role__name__in=["Establishment","Employee","Contractor"])
    

class EstablishmentEmployeeCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,EstablishmentRole]
    serializer_class = SuperadminUserSerializer

    def get_queryset(self):
        return User.objects.filter(user_role__role__name = 'Employee')
    
class EstablishmentEmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, EstablishmentRole]
    serializer_class = SuperadminUserSerializer

    def get_queryset(self):
        return User.objects.filter(user_role__role__name = 'Employee')



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer



    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username ,password = password)


        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh':str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            } 
            )
        else:
            return Response({'detail':'Invalid Credentials'},status=401)

class DasboardAdminView(APIView):
    permission_classes = (IsAuthenticated,AdminRole)

    def get(self, request):
        user_serializer = UserSerializer(request.user) 
        return Response({
            'message':'Welcome to Admin Dashboard',
            'user': user_serializer.data
        }, 200)  


class DasboardEstablishmentView(APIView):
    permission_classes = (IsAuthenticated,EstablishmentRole)

    def get(self, request):
        user_serializer = UserSerializer(request.user) 
        return Response({
            'message':'Welcome to Establishment Dashboard',
            'user': user_serializer.data
        }, 200)     


class DasboardEmployeeView(APIView):
    permission_classes = (IsAuthenticated,EmployeeRole)

    def get(self, request):
        user_serializer = UserSerializer(request.user) 
        return Response({
            'message':'Welcome to Employee Dashboard',
            'user': user_serializer.data
        }, 200)  

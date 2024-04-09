from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer,CarSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from app_api.models import CustomToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from app_api.models import Car
from rest_framework import permissions


@api_view(["POST"])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data["username"] = account.username
            data["password"] = account.password
            token = Token.objects.get(user= account).key
            data["token"] = token
        return Response(data)
    

class LoginView(APIView):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            active_session = CustomToken.objects.filter(user=user).first()
            print(active_session)
            if active_session:
                return JsonResponse({'error': 'User already logged in'}, status=400)
            login(request, user)

            token, _ = Token.objects.get_or_create(user=user)
            CustomToken.objects.create(user=user, token=token)
            return JsonResponse({'token': token.key})
        else:
            return HttpResponse('Invalid credentials', status=400)
        


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class UserCarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Car.objects.filter(user=user)

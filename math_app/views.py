from django.contrib.sites import requests

from math_project import settings
from .repositories.models_repository import PlayerRepository, TaskRepository, TypeRepository
from .serializers import PlayerTaskSerializer, UserRegistrationSerializer, PlayerSerializer, TaskSerializer

from django.utils import timezone

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from .services.player_service import PlayerService
from .services.task_service import TaskService
from .services.player_task_service import PlayerTaskService


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

class LogoutView(generics.GenericAPIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class PlayerTaskAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        player_tasks = PlayerTaskService.get_completed_player_tasks()
        serializer = PlayerTaskSerializer(player_tasks, many=True)
        return Response(serializer.data)

class HomeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        player = PlayerService.get_player_by_user(user)

        task_type = request.GET.get('task_type')

        if task_type:
            tasks = TaskService.get_tasks_by_type(task_type)
        else:
            tasks = TaskRepository.get_all()

        history_tasks = PlayerTaskService.get_player_task_history(player)
        task_types = TypeRepository.get_all()

        player_data = PlayerSerializer(player).data
        tasks_data = TaskSerializer(tasks, many=True).data
        completed_tasks_data = PlayerTaskSerializer(history_tasks, many=True).data

        context = {
            'player': player_data,
            'tasks': tasks_data,
            'history_tasks': completed_tasks_data,
            'task_type': task_type,
            'task_types': task_types,
        }

        return render(request, 'home.html', context)

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        user = request.user
        player = PlayerService.get_player_by_user(user)
        task = TaskRepository.get_by_id(task_id)
        player_task, created = PlayerTaskService.get_or_create_player_task(player, task)

        context = {
            'task': task,
            'player_task': player_task,
        }

        return render(request, 'task_detail.html', context)

    def post(self, request, task_id):
        user = request.user
        player = PlayerService.get_player_by_user(user)
        task = TaskRepository.get_by_id(task_id)
        player_task, created = PlayerTaskService.get_or_create_player_task(player, task)

        answer = request.POST.get('answer')

        message = TaskService.update_player_task(player_task,player,task,answer)

        context = {
            'task': task,
            'player_task': player_task,
            'message': message,
        }

        return render(request, 'task_detail.html', context)

class PlayerTaskAPIList(generics.ListAPIView):
    serializer_class = PlayerTaskSerializer
    permission_classes = (IsOwnerOrAdmin,)

    def get_queryset(self):
        user = self.request.user
        return PlayerTaskService.get_player_tasks_by_user(user.player.id)

class PlayerAPIList(generics.ListCreateAPIView):
    queryset = PlayerRepository.get_all()
    serializer_class = PlayerSerializer
    permission_classes = (IsAdminUser,)

class PlayerAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = PlayerRepository.get_all()
    serializer_class = PlayerSerializer
    permission_classes = (IsAdminUser,)

class PlayerAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = PlayerRepository.get_all()
    serializer_class = PlayerSerializer
    permission_classes = (IsAdminUser,)


class TaskAPIList(generics.ListCreateAPIView):
    queryset = TaskRepository.get_all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminOrReadOnly,)

class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = TaskRepository.get_all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminUser,)

class TaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = TaskRepository.get_all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminUser,)

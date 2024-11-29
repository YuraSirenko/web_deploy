"""
URL configuration for math_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from django.contrib import admin
from math_app.views import PlayerAPIList, PlayerAPIUpdate, PlayerAPIDestroy, UserRegistrationView, PlayerTaskAPIList, \
    TaskAPIList, HomeAPIView, TaskDetailView, LogoutView, UserRegistrationView, TaskAPIUpdate, TaskAPIDestroy

from django.urls import path, include
from dashboard.views import  dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', HomeAPIView.as_view(), name='home'),
    path('task/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
    path('playertasklist/', PlayerTaskAPIList.as_view()),

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('playerlist/', PlayerAPIList.as_view()),
    path('playerlist/<int:pk>/', PlayerAPIUpdate.as_view()),
    path('playerdelete/<int:pk>/', PlayerAPIDestroy.as_view()),

    path('tasklist/', TaskAPIList.as_view()),
    path('tasklist/<int:pk>/',TaskAPIUpdate.as_view()),
    path('taskdelete/<int:pk>/',TaskAPIDestroy.as_view()),

    path('dashboard/', dashboard_view, name='dashboard'),

]

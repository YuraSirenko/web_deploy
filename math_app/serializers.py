from django.core.serializers import serialize
from django.db.models import Model
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer, ModelSerializer

from math_app.models import Player, TaskAnswer, Task, PlayerTask, Type


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        Player.objects.create(user=user, name=user.username)

        return user

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class PlayerTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerTask
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class TaskAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAnswer
        fields = '__all__'


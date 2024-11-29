from django.contrib.auth.models import User
from math_app.models import Player, PlayerTask, Task


class PlayerService:
    @staticmethod
    def get_player_by_user(user: User) -> Player:
        return Player.objects.get(user=user)

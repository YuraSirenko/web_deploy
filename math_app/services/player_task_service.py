from math_app.models import PlayerTask, Player, Task
from django.contrib.auth.models import User

class PlayerTaskService:
    @staticmethod
    def get_player_task_history(player: Player):
        return PlayerTask.objects.filter(player=player).order_by('-last_updated')


    @staticmethod
    def get_or_create_player_task(player: Player, task: Task):
        return PlayerTask.objects.get_or_create(player=player, task=task)


    @staticmethod
    def get_player_tasks_by_user(user: User):
        return PlayerTask.objects.filter(player_id=user.player.id)


    @staticmethod
    def get_completed_player_tasks():
        return PlayerTask.objects.filter(completed=True)
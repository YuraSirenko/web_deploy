from django.utils import timezone

from math_app.models import Task, TaskAnswer


class TaskService:
    @staticmethod
    def get_tasks_by_type(task_type: str):
        return Task.objects.filter(type__name=task_type)

    @staticmethod
    def update_player_task(player_task, player, task, answer):
        correct_answer = TaskAnswer.objects.filter(task=task, answer=answer).exists()

        if player_task.completed:
            message = "You can't resubmit answer."
        elif correct_answer:
            player_task.completed = True
            player.high_score += task.max_score
            player.save()
            message = "Correct answer! Task completed."
        else:
            message = "Incorrect answer. Please try again."

        player_task.last_updated = timezone.now()
        player_task.save()

        return message
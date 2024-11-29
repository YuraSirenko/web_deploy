from math_app.models import Player, Type, Task, PlayerTask, TaskAnswer
from .base_repository import BaseRepository

class PlayerRepository(BaseRepository):
    model = Player

class TypeRepository(BaseRepository):
    model = Type

class TaskRepository(BaseRepository):
    model = Task

class PlayerTaskRepository(BaseRepository):
    model = PlayerTask

class TaskAnswerRepository(BaseRepository):
    model = TaskAnswer
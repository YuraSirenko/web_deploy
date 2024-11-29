from django.contrib import admin
from .models import Player, Type, Task, PlayerTask, TaskAnswer

admin.site.register(Player)
admin.site.register(Type)
admin.site.register(Task)
admin.site.register(PlayerTask)
admin.site.register(TaskAnswer)
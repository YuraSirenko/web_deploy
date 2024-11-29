from django.shortcuts import render
from django.db.models import Count
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from math_app.models import PlayerTask
import json

def dashboard_view(request):
    auth = JWTAuthentication()
    try:
        auth_result = auth.authenticate(request)
        if auth_result is None:
            raise AuthenticationFailed("Authentication failed")
        user, token = auth_result
    except AuthenticationFailed:
        return render(request, 'dashboard.html', {'data': json.dumps([]), 'player_name': ''})

    completed_tasks_by_type = PlayerTask.objects.filter(player__user=user, completed=True).values('task__type__name').annotate(count=Count('id'))
    data = list(completed_tasks_by_type)
    player_name = user.username
    context = {'data': json.dumps(data), 'player_name': player_name}

    return render(request, 'dashboard.html', context)
from rest_framework import status
from rest_framework.response import Response

from .models import Task
from django.http import JsonResponse
from .serializer import TaskSerializer, TaskRequestSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serialized = TaskSerializer(task, many=True)
        data = {
            'task': serialized.data
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        task = TaskSerializer(data=request.data)
        if task.is_valid():
            task.save()
            return Response(task.data, status=status.HTTP_201_CREATED)

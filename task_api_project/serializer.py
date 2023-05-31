from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    due_date = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'due_date')


class TaskRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description')

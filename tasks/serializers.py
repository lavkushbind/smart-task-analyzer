from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # Score hum alag se calculate karenge, isliye read_only rakha hai
    score = serializers.FloatField(read_only=True, required=False)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'due_date', 'estimated_hours', 'importance', 'dependencies', 'score']
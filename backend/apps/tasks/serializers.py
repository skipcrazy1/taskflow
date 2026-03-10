from rest_framework import serializers
from .models import Task, Comment
from apps.projects.models import Project

class TaskSerializer(serializers.ModelSerializer):
    project_detail = serializers.StringRelatedField(source="project", read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'headline', 'description', 'status', 'priority', 
                 'deadline', 'created_by', 'executer', 'project',
                 'project_detail', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'task', 'author', 'author_username', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']
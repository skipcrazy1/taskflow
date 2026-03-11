from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'created_by', 'username']
        read_only_fields = ['id', 'created_at']
        

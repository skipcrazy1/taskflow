from rest_framework import serializers
from .models import Profile


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'username', 'email', 'bio', 'telegram']
        read_only_fields = ['id']

from rest_framework import viewsets
from .models import Profile
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer
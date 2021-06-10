from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets, permissions
from alleyways.serializers import UserSerializer, ShardSerializer, ShardListSerializer
from alleyways.models import User, Shard, ShardList

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShardViewSet(viewsets.ModelViewSet):
    queryset = Shard.objects.all()
    serializer_class = ShardSerializer


class ShardListViewSet(viewsets.ModelViewSet):
    queryset = ShardList.objects.all()
    serializer_class = ShardListSerializer

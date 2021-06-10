from .models import Shard, ShardList, User
from rest_framework import serializers


class ShardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shard
        fields = '__all__'


class ShardListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShardList
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
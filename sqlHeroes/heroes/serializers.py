from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Power
        fields = ['name']

class Relationship_typeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relationship_type
        fields = ['name']

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    powers = PowerSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = ['name', 'about', 'bio', 'powers']

class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    relationship = Relationship_typeSerializer()
    hero1 = serializers.StringRelatedField()
    hero2 = serializers.StringRelatedField()
    

    class Meta:
        model = Relationship
        fields = ['hero1', 'hero2', 'relationship']


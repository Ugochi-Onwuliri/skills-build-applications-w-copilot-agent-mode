from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    members = serializers.ListField(child=serializers.CharField(max_length=255))

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()
    date = serializers.DateField()

class LeaderboardSerializer(serializers.Serializer):
    team = serializers.CharField(max_length=255)
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()

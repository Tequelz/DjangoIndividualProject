from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, LessonID, TeachingSession


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description','owner'
        )

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonID
        fields = (
            'lec_id','lec_name', 'lec_number' ,'lec_time', 'lec_teacher',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'username','email',
        )

class TeachingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingSession
        fields = (
            'username','lesson_id',
        )

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    lec_name = serializers.CharField(max_length=100)
    lec_number = serializers.IntegerField()
    lec_time = serializers.DateTimeField()
    lec_teacher = serializers.IntegerField()
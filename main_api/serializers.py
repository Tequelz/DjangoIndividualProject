from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Module, LectureSession, Lecture


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = (
            'mod_teacher','mod_name','mod_id',
            )

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = (
            'lec_id','lec_number', 'lec_length',
        )

class LectureSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureSession
        fields = (
            'username','lecture_id',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'username','email',
        )
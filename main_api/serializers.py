from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Module, LectureSession, Lecture


class ModuleSerializer(serializers.ModelSerializer): ##This serializer supports the encoding and decoding of Modules in python with the stated fields
    class Meta:
        model = Module
        fields = (
            'mod_teacher','mod_name','mod_id',
            )

class LectureSerializer(serializers.ModelSerializer): ##This serializer supports the encoding and decoding of Lectures in python with the stated fields
    class Meta:
        model = Lecture
        fields = (
            'lec_id','lec_number', 'lec_length',
        )

class LectureSessionSerializer(serializers.ModelSerializer):  ##This serializer supports the encoding and decoding of LectureSessions in python with the stated fields
    class Meta:
        model = LectureSession
        fields = (
            'username','lecture_id',
        )


class UserSerializer(serializers.ModelSerializer): ##This serializer supports the encoding and decoding of User models in python with the stated fields
    class Meta:
        model = get_user_model()
        fields = (
            'username','email',
        )
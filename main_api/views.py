import json
from itertools import chain

from django.shortcuts import render
from django.http import JsonResponse, request
# Create your views here.

#third party api
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth import get_user_model


from .serializers import UserSerializer, LectureSessionSerializer, ModuleSerializer, LectureSerializer
from .models import LectureSession, Module, Lecture


class GetUserDetails(generics.ListCreateAPIView):

    permission_classes = (IsAdminUser,)

    serializer_class = UserSerializer


    def post(self, request, *args, **kwargs):
        User = get_user_model()
        qs = User.objects.filter(pk=request.data.get("userID"))

        serializer = UserSerializer(qs, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)


class ModuleCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAdminUser,)

    serializer_class = ModuleSerializer

    def get_queryset(self):
        user = self.request.user

        return Module.objects.filter(mod_teacher=user)

class LectureView(generics.ListCreateAPIView):

    permission_classes = (IsAdminUser,)

    serializer_class = LectureSerializer
    # queryset = Lecture.objects.all()

    def post(self, request, *args, **kwargs):
        qs = Lecture.objects.filter(lec_id=request.data.get("lecID"))

        serializer = LectureSerializer(qs, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

class LectureCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAdminUser,)

    serializer_class = LectureSerializer
    # queryset = Lecture.objects.all()


class LectureIDCheck(generics.ListCreateAPIView):

    serializer_class = LectureSerializer

    def post(self, request, *args, **kwargs):
        qs = list(Lecture.objects.filter(lec_id= request.data.get("lec_id"),lec_number= request.data.get("lec_number"),lec_length=request.data.get("lec_length")).values('pk'))

        # serializer = LectureSerializer(qs, many=True)
        # data = serializer.data
        return JsonResponse(qs, safe=False)

class LectureSessionByModule(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)

    serializer_class = LectureSessionSerializer
    queryset = LectureSession.objects.all()

    def post(self, request, *args, **kwargs):
        qs = LectureSession.objects.filter(lecture_id=request.data.get("code"))

        serializer = LectureSessionSerializer(qs, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)



class LectureSessionCreateView(generics.ListCreateAPIView):
    serializer_class = LectureSessionSerializer
    queryset = LectureSession.objects.all()








    # def get(self, request, *args, **kwargs):
    #     qs = LectureSession.objects.filter(lecture_id = request.data.get('lec_id'))
    #     serializer = LectureSessionSerializer(qs,many=True)
    #     data = serializer.data
    #     return JsonResponse(data, safe=False)






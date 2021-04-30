import json
from itertools import chain

from django.shortcuts import render
from django.http import JsonResponse, request
# Create your views here.

#third party api

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth import get_user_model



from .serializers import PostSerializer, LessonSerializer, TeachingSessionSerializer, RegisterSerializer
from .models import Post, LessonID, TeachingSession, user


# class TestView(APIView):
#
#     permission_classes = (IsAuthenticated, )
#
#     def get(self,request,*args,**kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         #serializer = PostSerializer(qs,many=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)



class PostView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(self,request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class TeachingSessionCreateView(generics.ListCreateAPIView):
    serializer_class = TeachingSessionSerializer
    queryset = TeachingSession.objects.all()

    def get(self, request, *args, **kwargs):
        qs = TeachingSession.objects.filter(lesson_id=request.data.get("code"))

        serializer = TeachingSessionSerializer(qs,many=True)
        data = serializer.data
        return JsonResponse(data)




class LessonCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAdminUser,)

    serializer_class = LessonSerializer
    model = LessonID

    def get_queryset(self):
        user = self.request.user

        return LessonID.objects.filter(lec_teacher=user)


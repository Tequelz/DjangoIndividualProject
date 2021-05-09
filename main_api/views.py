from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from django.contrib.auth import get_user_model ## Imports are used to add security to the views while generics allows for the easy creation of these views

from .serializers import UserSerializer, LectureSessionSerializer, ModuleSerializer, LectureSerializer
from .models import LectureSession, Module, Lecture ##Import the models and serializers from the other files for use here


class GetUserDetails(generics.ListCreateAPIView):
    """
    Class that can be used by staff for getting a user's details from just their id via a POST request
    """

    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        User = get_user_model()
        qs = User.objects.filter(pk=request.data.get("userID"))

        serializer = UserSerializer(qs, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)


class ModuleCreateView(generics.ListCreateAPIView):
    """
    Class that enables the creation of Modules or viewing of them limited to staff, here it has the option to return all modules associate to the user
    as well as the option to create a new module through the ModuleSerializer
    """

    permission_classes = (IsAdminUser,)
    serializer_class = ModuleSerializer

    def get_queryset(self):
        user = self.request.user

        return Module.objects.filter(mod_teacher=user)

class LectureView(generics.ListCreateAPIView):
    """
    Class that enables the viewing of lectures from a POST request by being a staff member and then passing in a lecture id value, which returns a JSON
    object of all lectures matching the filter
    """

    permission_classes = (IsAdminUser,)
    serializer_class = LectureSerializer

    def post(self, request, *args, **kwargs):
        qs = Lecture.objects.filter(lec_id=request.data.get("lecID"))

        serializer = LectureSerializer(qs, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

class LectureCreateView(generics.ListCreateAPIView):
    """
    Class that enables the creation of Lectures via a POST request and the LectureSerializer restircted to only staff
    """

    permission_classes = (IsAdminUser,)
    serializer_class = LectureSerializer

class LectureIDCheck(generics.ListCreateAPIView):
    """
    Class that is used to return a lecture's id from the corresponding entered values for that lecture sent via a POST request, the
    user must be logged in to use this view
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = LectureSerializer

    def post(self, request, *args, **kwargs):
        qs = list(Lecture.objects.filter(lec_id= request.data.get("lec_id"),lec_number= request.data.get("lec_number"),lec_length=request.data.get("lec_length")).values('pk'))

        return JsonResponse(qs, safe=False)

class LectureSessionByModule(generics.ListCreateAPIView):
    """
    Class that can obtain all the LectureSessions via a POST request that matches a module_id as this is equal to lec_id, this returns a list of usernames associated with
    that Lecture
    """

    permission_classes = (IsAdminUser,)
    serializer_class = LectureSessionSerializer

    def post(self, request, *args, **kwargs):
        qs = LectureSession.objects.filter(lecture_id=request.data.get("code"))

        serializer = LectureSessionSerializer(qs, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

class LectureSessionCreateView(generics.ListCreateAPIView):
    """
    Class that is used by the users to create a LectureSession of their name and the lecture_id, meaning they can now be found via a mod_id filter on the
    LectureSession models
    """

    permission_classes = (IsAuthenticated,)

    serializer_class = LectureSessionSerializer
    queryset = LectureSession.objects.all()






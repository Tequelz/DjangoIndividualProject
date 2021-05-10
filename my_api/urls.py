
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token


from main_api.views import GetUserDetails, ModuleCreateView, LectureSessionCreateView, LectureCreateView, \
    LectureIDCheck, \
    LectureView, LectureSessionByModule ##Obtain all the views from the file, and then create some paths with them

urlpatterns = [
    path('api-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls), ##Used for the admin page
    path('module-create/',ModuleCreateView.as_view(),name="create-module"), #Used to create and view modules
    path('lecture-create/',LectureCreateView.as_view(),name="create-lecture"), #Used to create Lectures
    path('lecture-view/',LectureView.as_view(),name="view-lecture"), #Used to view some lectures
    path('lecture-check/',LectureIDCheck.as_view(),name="id-check"), #Used to get the id of a certain lecture
    path('user-attend/',LectureSessionCreateView.as_view(),name="add-student"), #Used to create a LectureSession for signing a user in
    path('class-attendance/',LectureSessionByModule.as_view(),name="attendance"), #Used to get the students who have registered into a lecture
    path('get-user-by-id/',GetUserDetails.as_view(),name="get-user"), #Used to get the user's details from their id
    path('api/token/',obtain_auth_token,name='obtain-token'), ##Used to get the auth token of the user
    path('rest-auth/',include('rest_auth.urls')), #Allows for the user of rest-auth paths
    path('rest-auth/registration/',include('rest_auth.registration.urls')), #Allows for the registering of new users via a request

]

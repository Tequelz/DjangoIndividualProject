
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from main_api.views import PostView, PostCreateView, PostListCreateView, LessonCreateView, TeachingSessionCreateView, \
    GetUserDetails

urlpatterns = [
    path('api-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('',PostView.as_view(),name="test"),
    path('create/',PostCreateView.as_view(),name="create"),
    path('list-create/',PostListCreateView.as_view(),name="create-list"),
    path('lesson-create/',LessonCreateView.as_view(),name="create-teach-session"),
    path('user-attend/',TeachingSessionCreateView.as_view(),name="add-student"),
    path('get-user-by-id/',GetUserDetails.as_view(),name="get-user"),
    path('api/token/',obtain_auth_token,name='obtain-token'),
    path('rest-auth/',include('rest_auth.urls')),
    path('rest-auth/registration/',include('rest_auth.registration.urls')),

]

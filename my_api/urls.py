
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token


from main_api.views import GetUserDetails, ModuleCreateView, LectureSessionCreateView, LessonCreateView

urlpatterns = [
    path('api-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('module-create/',ModuleCreateView.as_view(),name="create-module"),
    path('lecture-create/',LessonCreateView.as_view(),name="create-lecture"),
    path('user-attend/',LectureSessionCreateView.as_view(),name="add-student"),
    path('get-user-by-id/',GetUserDetails.as_view(),name="get-user"),
    path('api/token/',obtain_auth_token,name='obtain-token'),
    path('rest-auth/',include('rest_auth.urls')),
    path('rest-auth/registration/',include('rest_auth.registration.urls')),

]

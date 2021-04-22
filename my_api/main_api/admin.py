from django.contrib import admin

# Register your models here.


from .models import Post, LessonID, TeachingSession

admin.site.register(Post)
admin.site.register(TeachingSession)
admin.site.register(LessonID)
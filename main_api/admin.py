from django.contrib import admin

# Register your models here.


from .models import Module, Lecture, LectureSession

admin.site.register(Module)
admin.site.register(Lecture)
admin.site.register(LectureSession)
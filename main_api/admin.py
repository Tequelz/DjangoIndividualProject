from django.contrib import admin

from .models import Module, Lecture, LectureSession ##import related views from the models file

admin.site.register(Module) ##Allow for these models to be viewed and changed on the admin portal
admin.site.register(Lecture)
admin.site.register(LectureSession)
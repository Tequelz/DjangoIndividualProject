from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

class Module(models.Model):
    mod_teacher = models.ForeignKey(user, on_delete=models.CASCADE)
    mod_name = models.CharField(max_length=100)
    mod_id = models.IntegerField(primary_key=True)
    mod_course = models.CharField(max_length=100)

class Lecture(models.Model):
    lec_id = models.ForeignKey(Module,on_delete=models.CASCADE)
    lec_number = models.IntegerField()
    lec_length = models.IntegerField()
    lec_time = models.DateTimeField(auto_now_add=True)

class LectureSession(models.Model):
    username =models.ForeignKey(user,on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(Lecture,on_delete=models.CASCADE,default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'lecture_id'], name='unique_sign_in'),
        ]

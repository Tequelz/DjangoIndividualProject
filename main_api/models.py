from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(user,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class LessonID(models.Model):
    lec_id = models.IntegerField(primary_key=True)
    lec_name = models.CharField(max_length=100)
    lec_number = models.IntegerField()
    lec_time = models.DateTimeField(auto_now_add=True)
    lec_teacher = models.ForeignKey(user,on_delete=models.CASCADE)

class TeachingSession(models.Model):
    username =models.ForeignKey(user,on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(LessonID,on_delete=models.CASCADE,default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        models.UniqueConstraint(fields=['username','lesson_id'],name='unique_sign_in')
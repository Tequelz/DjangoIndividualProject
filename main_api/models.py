from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model() ## create an instance of get_user_model called user

class Module(models.Model):
    """
    Model that allows for the creation of modules taking in information for all the corresponding fields with mod_id acting as the key
    """
    mod_id = models.IntegerField(primary_key=True,max_length=5)
    mod_teacher = models.ForeignKey(user, on_delete=models.CASCADE)
    mod_name = models.CharField(max_length=100)


class Lecture(models.Model):
    """
    Model that allows for lectures to be made, here each lecture is connected to a Module on the lec_id foreign key. And the constraints for lec_id and lec_number
    are said to be unique meaning a object of the model cannot have the same pair
    """
    lec_id = models.ForeignKey(Module,on_delete=models.CASCADE)
    lec_number = models.IntegerField(max_length=2)
    lec_length = models.IntegerField(max_length=3)
    lec_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['lec_id', 'lec_number'], name='unique_lecture'),
        ]

class LectureSession(models.Model):
    """
    Model that allows for the creation of a LectureSession which is used to register the user to a lecture, here the username and lecture_id are considered to
    be unique constraints together as a user should not be able to sign in twice
    """
    username = models.ForeignKey(user,on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(Lecture,on_delete=models.CASCADE,default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'lecture_id'], name='unique_sign_in'),
        ]

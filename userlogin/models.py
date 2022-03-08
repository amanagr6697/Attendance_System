from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField

# class details:


    
class image(models.Model):
    user_map=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to='images/', blank=True, null=True)
    facedata=PickledObjectField(default=None)

# class webcam(models.Model):
#     user_map=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
#     pic=models.ImageField(upload_to='images/', blank=True, null=True)
#     Department=models.CharField(max_length=100)
#     facedata=PickledObjectField(default=None)
    # def __str__(self):
    #  return self.user
    # class User(AbstractUser):
    #     Name=models.CharField(max_length=100)
    #     Roll_No=models.CharField(max_length=8,unique=True)
    #     College_Email=models.EmailField(unique=True)
    #     username=None

    #     USERNAME_FIELD='Roll_No'
    #     REQUIRED_FIELDS=[]

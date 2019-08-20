from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
user = models.OneToOneField(User,on_delete=models.CASCADE)
email = models.EmailField()
id= models.CharField(max_length=10)
topics= models.CharField(max_length=300)

def __str__(self):
  return self.user.username

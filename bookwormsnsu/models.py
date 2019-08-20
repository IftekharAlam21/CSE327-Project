from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=120)
    email=models.EmailField(max_length=300,unique=True)
    student_id= models.CharField(max_length=10,unique=True)
    topics= models.CharField(max_length=420)

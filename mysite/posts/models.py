from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
#POSTS models.py file

CATEGORY=(('sell','SELL'),('rent','RENT'))

class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts')
    title=models.TextField(max_length=200)
    published_date=models.DateTimeField(auto_now=True)
    price=models.TextField(max_length=20)
    message=models.TextField(max_length=500)
    category=models.CharField(max_length=6,choices=CATEGORY,default='sell')
    message_html=models.TextField(editable=False)
    group= models.ForeignKey(Group,related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.title

    def save(Self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url():
        return reverse('posts:single',kwargs={'username':self.user.usrname,'pk':self.pk})

    class Meta:
        ordering=['-created_at']
        unique_together=['user','message']

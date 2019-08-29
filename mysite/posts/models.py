from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone

import misaka

from django.contrib.auth import get_user_model
from accounts.models import User


# Create your models here.
#POSTS models.py file

CATEGORY=(('sell','SELL'),('rent','RENT'),('request','REQUEST'))

class Post(models.Model):
    user=models.ForeignKey(User,related_name="posts",null=True)
    title=models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)
    price=models.TextField(max_length=20)
    message=models.TextField(null=True)
    category=models.CharField(max_length=6,choices=CATEGORY,default='sell')
    message_html=models.TextField(editable=False)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def save(self,*args,**kwargs):
        #self.message_html=misaka.html(self.message)
        #super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    class Meta:
        ordering=['-published_date']
        unique_together=['user','message']

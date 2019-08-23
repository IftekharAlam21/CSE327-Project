from django.db import models
from django.urls import reverse
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.pk})

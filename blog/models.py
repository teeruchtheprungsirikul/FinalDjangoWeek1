from importlib.resources import contents
from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=80)
    short_description = models.TextField()
    content = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    featured_pic = models.ImageField(upload_to='cover', null=True, blank=True)
    
    def __str__(self) :
        return self.title
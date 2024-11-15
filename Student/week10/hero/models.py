from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy 

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField(default = "None")
    image = models.CharField(max_length=200,default = "None")
    strengths = models.CharField(max_length=200,default = "None")
    weaknesses = models.CharField(max_length=200,default = "None")


    def __str__(self):
        return self.identity
    def get_absolute_url(self):
        return reverse_lazy('hero_list')
    
from django.urls import reverse_lazy


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("article_list")

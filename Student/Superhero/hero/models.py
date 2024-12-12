#AC
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy 
from photos.models import Photo

class Investigator(models.Model):
    name = models.CharField(max_length=200, default='Def Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investigator', blank=True, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('investigator_list')
    

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField(default = "None")
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, blank=True)
    strengths = models.CharField(max_length=200,default = "None")
    weaknesses = models.CharField(max_length=200,default = "None")
    investigator = models.ForeignKey(Investigator, on_delete=models.CASCADE, related_name='superheroes', blank=True, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('hero_list')
    



class Article(models.Model):
    hero = models.ForeignKey(Superhero, null=True, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    body=models.TextField(max_length=5000, default= "no content")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("article_list")
        

class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy("message_list")
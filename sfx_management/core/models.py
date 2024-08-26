from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
class SoundEffect(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.FileField(upload_to='sfx_files/')
    games = models.ManyToManyField(Game)
    

    


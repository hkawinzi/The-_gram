from django.db import models

# Create your models here.
class Image(models.Model):
    Image_name = models.CharField (max_length=100)
    Image_caption = models.CharField(max_length=200)
    Likes = models.IntegerField(default=0)
    Comments = models.CharField(max_length=300)
    
   
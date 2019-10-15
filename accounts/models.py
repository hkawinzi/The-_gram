from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def __str__(self):
    return f'{self.user.username} Profile'
# Create your models here.


class Image(models.Model):
    Image_name = models.CharField(max_length=100)
    Image_caption = models.CharField(max_length=200)
    Likes = models.IntegerField(default=0)
    Comments = models.CharField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Image_name

    def save_image(self):
        self.save

    def delete_image(self):
        image = Image.objects.all().delete()
        return image


def __str__(self):
    return f'{self.user.username} Profile'


class Profile(models.Model):
    # creating a relationship with an existing user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} Profile'

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
class User(AbstractBaseUser):
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  email = models.CharField(max_length=60)

  USER_NAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

class Image(models.Model):
  title = models.CharField(max_length=40)
  artist_name = models.CharField(max_length=60)
  image_link = models.CharField(max_length=200)
  user = models.ForeignKey(User)

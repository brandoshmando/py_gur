from django.db import models

class User(models.Model):
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  email = models.CharField(max_length=60)

class Image(models.Model):
  title = models.CharField(max_length=40)
  artist_name = models.CharField(max_length=60)
  image_link = models.CharField()
  user = models.ForeignKey(User)

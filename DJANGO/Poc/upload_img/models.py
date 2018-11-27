from django.db import models

# Create your models here.
class Image(models.Model):
  image1 = models.ImageField(blank=True, upload_to='upload_img/', default='placeholder400x400.png')

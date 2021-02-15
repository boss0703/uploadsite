from django.db import models


class ImageFileModel(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    link = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

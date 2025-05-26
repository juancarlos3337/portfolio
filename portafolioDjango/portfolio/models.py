from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)

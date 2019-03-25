from django.db import models

# Create your models here.
class Gallery(models.Model):
    """Model definition for MODELNAME."""
    objects=models.Manager()
    description = models.CharField(max_length=50)
 


from django.db import models

# Create your models here.
class Gallery(models.Model):
    """Model definition for MODELNAME."""
    object=models.Manager()
    description=models.CharField(max_lenth=100)
 

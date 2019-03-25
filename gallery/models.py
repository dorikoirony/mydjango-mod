from django.db import models

# Create your models here.
class Gallery(models.Model):
    """Model definition for MODELNAME."""
    objects=models.Manager()
    description = models.CharField(default='请输入简介',max_length=100)
    image = models.ImageField(default='default.png',upload_to='images/')
    title = models.CharField(default='作品标题',max_length=50)
    
    def __str__(self):              #用于修改标题
        return self.title               


 


from django.db import models

# Create your models here.
class Blog(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    objects=models.Manager()
    title = models.CharField(default='文章标题', max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.png',upload_to='images/')
    text = models.TextField(default='文章正文')
    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.title
    def short_text(self):
        return self.text[0:100] + '...'

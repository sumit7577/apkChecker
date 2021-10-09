from django.db import models

# Create your models here.
class File(models.Model):
    fileName = models.FileField(upload_to="",blank=True)


    def __str__(self):
        return self.fileName.name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)
    reason = models.CharField(max_length=65535)


    def __str__(self):
        return str(self.name)
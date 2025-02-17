from django.db import models

# Create your models here.
class contactUsModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    message = models.TextField(max_length=800)
    
    def __str__(self):
        return self.name
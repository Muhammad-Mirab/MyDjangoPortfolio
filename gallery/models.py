from django.db import models

# Create your models here.
class categories(models.Model):
    categoryName = models.CharField(max_length=60)
    def __str__(self):
        return self.categoryName

class gallery(models.Model):
    photo = models.ImageField(upload_to='gallery')
    categoriesList = categories.objects.all()
    choices = []
    for i in categoriesList:
        choices.append((i.categoryName, i.categoryName))
    category = models.CharField(max_length=256, choices=choices, default="General")
    location = models.CharField(max_length=40)
    date = models.DateField()
    def __str__(self):
        return self.location

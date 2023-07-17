from django.db import models

# Create your models here.
class universityAndEducation(models.Model):
    uniName = models.CharField(max_length=100)
    startDate = models.DateField("starting time")
    endDate = models.DateField("ending time(blank for still going)")
    about = models.CharField(max_length=250)
    # def __str__(self):
    #     return self.uniName

class experiences(models.Model):
    name = models.CharField(max_length=100)
    startDate = models.IntegerField()
    endDate = models.IntegerField()
    about = models.CharField(max_length=250)

class skills(models.Model):
    name = models.CharField(max_length=50)
    percent = models.IntegerField()
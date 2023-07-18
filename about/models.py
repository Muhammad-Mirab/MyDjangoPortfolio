from django.db import models

# Create your models here.
class sideBarInfo(models.Model):
    name = models.CharField(max_length=50)
    jobTitle = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    birthday = models.DateField()
    location = models.TextField(max_length=40)

    linkedInLink = models.CharField(max_length=100)
    twitterLink = models.CharField(max_length=100)
    githubLink = models.CharField(max_length=100, null=True, blank=True, default="#")
    instagramLink = models.CharField(max_length=100)
    telegramLink = models.CharField(max_length=100)
    youtubeLink = models.CharField(max_length=100, null=True, blank=True, default="#")
    buyMeACoffeeLink = models.CharField(max_length=100, null=True, blank=True, default="#")

    def __str__(self):
        return self.name

class aboutMe(models.Model):
    text = models.TextField()

class whatIDo(models.Model):
    title = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='pics')
    info = models.CharField(max_length=80, default="yeah, nothing to say here...")
    def __str__(self):
        return self.title
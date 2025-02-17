from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=60)
    def __str__(self):
        return self.categoryName
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.categoryName


class Blog(models.Model):
    photo = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:blogDetail', kwargs={'title': self.title.replace(' ', '-').lower()})

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Blog", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author} on '{self.post}'"
from django.db import models

# Create your models here.

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=50)
    tag = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title

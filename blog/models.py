from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    show_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
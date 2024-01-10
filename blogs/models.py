from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """A Blog-post the author wants to create"""
    title = models.CharField(max_length=200)
    catch_phrase = models.TextField(default="Bla Bla")
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.title


class Comment(models.Model):
    """A comment to a blogpost"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return f'Comment by {self.author} on {self.post}'
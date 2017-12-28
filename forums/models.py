from django.db import models
from django.contrib.auth.models import User


class Subreddit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)

    subreddit = models.ForeignKey(Subreddit, related_name='posts', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    message = models.TextField(max_length=4000)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    #related_name='+' instructs django that we don't need reverse relationship

    def __str__(self):
        return self.name

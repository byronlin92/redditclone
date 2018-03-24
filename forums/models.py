from django.db import models
from django.contrib.auth.models import User

class Subreddit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_post_count(self):
        return Post.objects.filter(subreddit=self).count()

    def get_total_comments(self):
        return Comment.objects.filter(post__subreddit=self).count()

    def get_last_post(self):
        return Post.objects.filter(subreddit=self).order_by('-created_at').first()

    def get_post_by_updated_by(self):
        return Post.objects.filter(subreddit=self).order_by('-created_at')


class Post(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=256)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='documents/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    subreddit = models.ForeignKey(Subreddit, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_parent_comments(self):
        return Comment.objects.filter(post=self, parent__isnull=True)


class Comment(models.Model):
    comment = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE) #related_name='+' instructs django that we don't need reverse relationship
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_child_comments(self):
        return Comment.objects.filter(parent=self)

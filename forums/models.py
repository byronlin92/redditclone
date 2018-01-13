from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
        return Post.objects.filter(subreddit=self).order_by('-last_updated').first()

    def get_post_by_updated_by(self):
        return Post.objects.filter(subreddit=self).order_by('-last_updated')

class Post(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)

    subreddit = models.ForeignKey(Subreddit, related_name='posts', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.subject


class Comment(models.Model):
    message = models.TextField(max_length=4000)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    #related_name='+' instructs django that we don't need reverse relationship

    def __str__(self):
        return self.message

from django import forms
from .models import Post, Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'url', 'image']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


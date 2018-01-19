from django import forms
from .models import Post, Comment

class NewPostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(),
        max_length=255,
        help_text='The max length of the text is 255.'
    )

    class Meta:
        model = Post
        fields = ['subject', 'message']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


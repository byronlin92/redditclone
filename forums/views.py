from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Subreddit, Post, Comment, User
from .forms import NewPostForm, NewCommentForm


def home(request):
    return render(request, 'home.html')

#SUBREDDITS
def subreddits(request):
    subreddits = Subreddit.objects.all()
    return render(request, 'subreddits.html', {'subreddits': subreddits})


#POSTS
def subreddit_posts(request, subreddit_name):
    subreddit = Subreddit.objects.get(name=subreddit_name)
    return render(request, 'subreddit_posts.html', {'subreddit': subreddit})

@login_required
def new_post(request, subreddit_name):
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.subreddit = subreddit
            post.starter = request.user
            post.save()
            comment = Comment.objects.create(
                message=form.cleaned_data.get('message'),
                post=post,
                created_by=request.user
            )
            return redirect('post_comments', subreddit_name=subreddit.name, post_pk=post.pk)
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'subreddit': subreddit, 'form': form})


#COMMENTS
def post_comments(request, subreddit_name, post_pk):
    post = Post.objects.get(pk=post_pk, subreddit__name=subreddit_name)
    return render(request, 'post_comments.html', { 'post': post})

@login_required
def new_comment(request, subreddit_name, post_pk):
    post = get_object_or_404(Post, pk=post_pk, subreddit__name=subreddit_name)

    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created_by = request.user
            comment.updated_at = timezone.now()
            comment.created_at = timezone.now()
            comment.save()
            return redirect('post_comments', subreddit_name=subreddit_name , post_pk=post_pk)  # TODO
    else:
        form = NewCommentForm()
    return render(request, 'new_comment.html', { 'post': post, 'form': form})



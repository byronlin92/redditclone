from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Subreddit, Post, Comment, User
from .forms import NewPostForm, NewCommentForm


def home(request):
    return render(request, 'home.html')

#SUBREDDITS
def subreddits(request):
    subreddits = Subreddit.objects.all().order_by('name')
    return render(request, 'subreddits.html', {'subreddits': subreddits})

#POSTS
def subreddit_posts(request, subreddit_name):
    subreddit = Subreddit.objects.get(name=subreddit_name)
    return render(request, 'subreddit_posts.html', {'subreddit': subreddit})

@login_required
def post_new(request, subreddit_name):
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.subreddit = subreddit
            post.created_by = request.user
            post.save()
            return redirect('post_comments', subreddit_name=subreddit.name, post_pk=post.pk)
    else:
        form = NewPostForm()
    return render(request, 'post_new.html', {'subreddit': subreddit, 'form': form})


#COMMENTS
def post_comments(request, subreddit_name, post_pk):
    post = Post.objects.get(pk=post_pk, subreddit__name=subreddit_name)
    return render(request, 'post_comments.html', { 'post': post})

@login_required
def comment_new(request, subreddit_name, post_pk):
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
            return redirect('post_comments', subreddit_name=subreddit_name , post_pk=post_pk)
    else:
        form = NewCommentForm()
    return render(request, 'comment_new.html', { 'post': post, 'form': form})

@login_required
def comment_update(request, subreddit_name, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, post__subreddit__name=subreddit_name, post__pk=post_pk)

    if request.method == 'POST' and 'Edit_comment' in request.POST:
        form = NewCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.updated_at = timezone.now()
            comment.save()
            return redirect('post_comments', subreddit_name=subreddit_name , post_pk=post_pk)
    #DELETE COMMENT
    elif request.method == 'POST' and 'Delete_comment' in request.POST:
        comment.delete()
        return redirect('post_comments', subreddit_name=subreddit_name, post_pk=post_pk)
    else:
        form = NewCommentForm()

    return render(request, 'comment_update.html', { 'comment': comment, 'form': form})

@login_required
def comment_reply(request, subreddit_name, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, post__subreddit__name=subreddit_name, post__pk=post_pk)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.parent = comment
            new_comment.post = comment.post
            new_comment.created_by = request.user
            new_comment.updated_by = request.user
            new_comment.created_at = timezone.now()
            new_comment.updated_at = timezone.now()
            new_comment.save()
            return redirect('post_comments', subreddit_name=subreddit_name , post_pk=post_pk)
    else:
        form = NewCommentForm()
    return render(request, 'comment_reply.html', { 'comment': comment, 'form': form})








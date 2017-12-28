from django.shortcuts import render, redirect, get_object_or_404
from .models import Subreddit, User, Comment
from .forms import NewPostForm

def home(request):
    return render(request, 'home.html')

def subreddits(request):
    subreddits = Subreddit.objects.all()
    return render(request, 'subreddits.html', {'subreddits': subreddits})

def subreddit_posts(request, name):
    subreddit = Subreddit.objects.get(name=name)
    return render(request, 'posts.html', {'subreddit': subreddit})

def new_post(request, subreddit_name):
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.subreddit = subreddit
            post.starter = user
            post.save()
            comment = Comment.objects.create(
                message=form.cleaned_data.get('message'),
                post=post,
                created_by=user
            )
            return redirect('subreddit_posts', name=subreddit.name)  # TODO: redirect to the created topic page
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'subreddit': subreddit, 'form': form})

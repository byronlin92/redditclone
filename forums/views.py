from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .models import Subreddit, Post, Comment, User
from .forms import NewPostForm


def home(request):
    return render(request, 'home.html')

#SUBREDDITS
class SubredditListView(ListView):
    model = Subreddit
    context_object_name = 'subreddits'
    template_name='subreddits.html'
    paginate_by = 20


#POSTS
class PostListView(ListView):
    model = Post
def subreddit_posts(request, subreddit_name):
    subreddit = Subreddit.objects.get(name=subreddit_name)
    return render(request, 'posts.html', {'subreddit': subreddit})


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
            return redirect('subreddit_posts', name=subreddit.name)  # TODO: redirect to the created topic page
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'subreddit': subreddit, 'form': form})


# class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'posts.html'
#     paginate_by = 20
#
#     def get_context_data(self, **kwargs):
#         kwargs['subreddit'] = self.subreddit
#         return super().get_context_data(**kwargs)
#
#     # def get_queryset(self):
#     #     self.subreddit = get_object_or_404(Subreddit, pk=self.kwargs.get('pk'))
#     #     queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
#     #     return queryset
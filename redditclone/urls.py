"""redditclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from forums import views
from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    #SUBREDDITS
    url(r'^subreddits/$', views.subreddits, name='subreddits'),


    #POSTS
    url(r'^r/(?P<subreddit_name>\w+)/$', views.subreddit_posts, name='subreddit_posts'),  #list
    url(r'^r/(?P<subreddit_name>\w+)/new/$', views.post_new, name='post_new'), #create
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/update/$', views.PostUpdateView.as_view(), name='update_post'),#update
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='delete_post'),#delete


    #COMMENTS
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/$', views.post_comments, name='post_comments'),  #list
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/new/$', views.comment_new, name='comment_new'), #create
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/comments/(?P<comment_pk>\d+)/update/$', views.comment_update, name='comment_update'),  #update
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/comments/(?P<comment_pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),  # update

    #REGISTRATION
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^settings/account/$', account_views.update_profile, name='my_account'),
    url(r'^admin/', admin.site.urls),

    #CHANGE PASSWORD
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
]

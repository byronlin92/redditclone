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
    url(r'^subreddits/$', views.SubredditListView.as_view(), name='subreddits'),

    # url(r'^subreddits/$', views.subreddits, name='subreddits'),

    # subreddits  #create/update/delete will be done by admin
    url(r'^r/(?P<subreddit_name>\w+)/$', views.subreddit_posts, name='subreddit_posts'), #list

    # posts
    url(r'^r/(?P<subreddit_name>\w+)/new/$', views.new_post, name='new_post'), #create
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/update/$', views.PostUpdateView.as_view(), name='update_post'),#update
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='delete_post'),#delete


    #comments
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/$', views.CommentListView.as_view(), name='list_comments'),  # list view
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/new/$', views.CommentCreateView.as_view(), name='new_comment'), #create
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/comments/(?P<comment_pk>\d+)/update/$', views.CommentUpdateView.as_view(), name='update_comment'),  #update
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/comments/(?P<comment_pk>\d+)/delete/$', views.CommentDeleteView.as_view(), name='delete_comment'),  # update

    #registration
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
        #Changing password
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    url(r'^settings/account/$', account_views.UserUpdateView.as_view(), name='my_account'),


    url(r'^admin/', admin.site.urls),
]

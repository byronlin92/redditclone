from django.conf.urls import url
from django.contrib import admin
from forums import views
from accounts import views as account_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # SUBREDDITS
    url(r'^subreddits/$', views.subreddits, name='subreddits'),

    # POSTS
    url(r'^r/(?P<subreddit_name>\w+)/$', views.subreddit_posts, name='subreddit_posts'),  # list
    url(r'^r/(?P<subreddit_name>\w+)/new/$', views.post_new, name='post_new'),  # create
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/update/$', views.PostUpdateView.as_view(), name='update_post'),#updatez
    # url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='delete_post'),#delete

    # VOTE POST
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/upvote/$', views.upvote_post, name='upvote_post'),
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/downvote/$', views.downvote_post, name='downvote_post'),

    # COMMENTS
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/$', views.post_comments, name='post_comments'),  # list
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/new/$', views.comment_new, name='comment_new'),  # create
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/comments/(?P<comment_pk>\d+)/update/$',
        views.comment_update, name='comment_update'),
    # update
    url(r'^r/(?P<subreddit_name>\w+)/posts/(?P<post_pk>\d+)/comments/(?P<comment_pk>\d+)/reply/$', views.comment_reply,
        name='comment_reply'),  # reply

    # REGISTRATION
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^account/(?P<account_username>\w+)/$', account_views.account_detail, name='account_detail'),
    url(r'^account/(?P<account_username>\w+)/update$', account_views.account_update, name='account_update'),
    url(r'^admin/', admin.site.urls),

    # CHANGE PASSWORD
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    # PROFILE
    url(r'^profile/(?P<profile_pk>\d+)/$', account_views.profile_detail, name='profile_detail'),
    url(r'^profile/(?P<profile_pk>\d+)/update$', account_views.profile_update, name='profile_update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.test import TestCase
from django.urls import resolve, reverse
from forums.views import comment_new
from forums.models import Subreddit, Post, Comment
from django.contrib.auth.models import User


class CommentsTests(TestCase):
    def setUp(self):
        subreddit = Subreddit.objects.create(name='django', description='description.')
        user= User.objects.create_user(username='byron', email='byron@live.com', password='123')
        Post.objects.create(name='postname', description='description', created_by=user, subreddit=subreddit)
        self.client.login(username='byron', password='123')

    def test_new_comment_view_success_status_code(self):
        url = reverse('comment_new', kwargs={'subreddit_name': 'django', 'post_pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_comment_url_resolves_new_comment_view(self):
        view = resolve('/r/django/posts/1/new/')
        self.assertEquals(view.func, comment_new)

    def test_new_comment_valid_post_data(self):
        url = reverse('comment_new', kwargs={'subreddit_name': 'django', 'post_pk': 1})
        data = {
            'comment': 'name'
        }
        self.client.post(url, data)
        self.assertTrue(Comment.objects.exists())

    def test_new_comment_invalid_post_data(self):
        # send form with without data
        url = reverse('comment_new', kwargs={'subreddit_name': 'django', 'post_pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

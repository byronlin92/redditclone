from django.test import TestCase
from django.urls import resolve, reverse
from forums.views import post_new
from forums.models import Subreddit, Post
from django.contrib.auth.models import User


class PostsTests(TestCase):
    def setUp(self):
        Subreddit.objects.create(name='django', description='description.')
        User.objects.create_user(username='byron', email='byron@live.com', password='123')
        self.client.login(username='byron', password='123')

    def test_new_post_view_success_status_code(self):
        url = reverse('post_new', kwargs={'subreddit_name': 'django'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_post_url_resolves_new_post_view(self):
        view = resolve('/r/django/new/')
        self.assertEquals(view.func, post_new)

    def test_new_post_valid_post_data(self):
        url = reverse('post_new', kwargs={'subreddit_name': 'django'})
        data = {
            'name': 'name',
            'description': 'description'
        }
        self.client.post(url, data)
        self.assertTrue(Post.objects.exists())

    def test_new_post_invalid_post_data(self):
        # send form with without data
        url = reverse('post_new', kwargs={'subreddit_name': 'django'})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

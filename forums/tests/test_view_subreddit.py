from django.test import TestCase
from django.urls import resolve, reverse
from forums.views import subreddit_posts
from forums.models import Subreddit

class SubredditTests(TestCase):
    def setUp(self):
        Subreddit.objects.create(name='django', description='description.')

    def test_subreddit_view_success_status_code(self):
        url = reverse('subreddit_posts', kwargs={'subreddit_name':'django'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_subreddit_url_resolves_subreddit_view(self):
        view = resolve('/r/django/')
        self.assertEquals(view.func, subreddit_posts)



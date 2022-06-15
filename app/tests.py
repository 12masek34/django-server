from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from app.views import index


class IndexPageText(TestCase):
    """Test home page"""

    def test_root_url_resolves_to_home_page_view(self):
        """Test source urls in index page"""
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        """test corrct returns html """
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

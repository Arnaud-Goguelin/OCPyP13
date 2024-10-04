from django.test import TestCase, Client
from django.urls import reverse


class LandingViewTests(TestCase):
    """
    Tests for the landing page view functionality.

    """

    def setUp(self):
        """
        Sets up the test client to simulate HTTP requests.
        """
        self.client = Client()

    def test_index_view(self):
        """
        Tests the index view by making a GET request to the landing page URL.
        Asserts that the status code is 200 (OK) and the 'index.html' template is used.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

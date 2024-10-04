from django.test import TestCase, Client
from django.urls import reverse


class LandingViewTests(TestCase):
    def setUp(self):
        # set up client to simulate htpp request
        self.client = Client()

    def test_index_view(self):
        """Test the index view"""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

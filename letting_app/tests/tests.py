from django.test import TestCase, Client
from django.urls import reverse

from letting_app.models import Address, Letting


class LettingViewTests(TestCase):
    def setUp(self):
        # set up client to simulate htpp request
        self.client = Client()

        # set up data to display in html rendered template
        self.address = Address.objects.create(
            number=123,
            street="test street",
            city="test city",
            state="test state",
            zip_code=12345,
            country_iso_code="test iso code",
        )
        self.letting = Letting.objects.create(
            title="Test Letting", address=self.address
        )

    def test_index_view(self):
        """Test the index view"""
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "letting_app/index.html")

    def test_lettings_view(self):
        """Test the lettings view"""
        response = self.client.get(reverse("letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "letting_app/letting.html")
        # make sure generated html template contain test letting title: "Test Letting"
        self.assertContains(response, self.letting.title)

from django.test import TestCase, Client
from django.urls import reverse

from profile_app.models import Profile
from django.contrib.auth.models import User


class ProfileViewTests(TestCase):
    def setUp(self):
        # set up client to simulate htpp request
        self.client = Client()

        # set up data to display in html rendered template
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(
            user=self.user, favorite_city="test favorite city"
        )

    def test_index_view(self):
        """Test the index view"""
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile_app/index.html")

    def test_profiles_view(self):
        """Test the profiles view"""
        response = self.client.get(
            reverse("profile", args=[self.profile.user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile_app/profile.html")
        # make sure generated html template contain test favorite city of test profile: "test favorite city"
        self.assertContains(response, self.profile.favorite_city)

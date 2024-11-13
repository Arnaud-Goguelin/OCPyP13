from django.test import TestCase, Client
from django.urls import reverse

from profile_app.models import Profile
from django.contrib.auth.models import User


class ProfileViewTests(TestCase):
    """
    Test suite for the Profile views.
    """

    def setUp(self):
        """
        Sets up the test client and creates a test user and profile for testing views.
        """
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
        """
        Tests the 'profiles_index' view to ensure it returns a status code of 200
        and uses the correct template.
        """
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile_app/index.html")

    def test_profiles_view(self):
        """
        Tests the 'profile' view for a specific user to ensure it returns a status code of 200,
        uses the correct template, and contains the test profile's favorite city.
        """
        response = self.client.get(
            reverse("profile", args=[self.profile.user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile_app/profile.html")
        # make sure generated html template contain
        # test favorite city of test profile: "test favorite city"
        self.assertContains(response, self.profile.favorite_city)

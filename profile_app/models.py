from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile linked to a user with a favorite city.

    Attributes:
        user (OneToOneField): The associated user from Django's built-in User model.
        favorite_city (str): A string representing the user's favorite city. Optional field.

    Meta:
        db_table (str): Specifies the custom database table name "oc_lettings_site_profile".

    Methods:
        __str__: Returns the username of the associated user for display purposes.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = "oc_lettings_site_profile"

    def __str__(self):
        return self.user.username

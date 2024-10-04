from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address entity with details about location and postal information.

    Attributes:
        number (PositiveIntegerField): The number of the building in the street.
        street (CharField): The street name.
        city (CharField): The city of the address.
        state (CharField): The state code (2 letters).
        zip_code (PositiveIntegerField): The postal code for the address.
        country_iso_code (CharField): The ISO code of the country (3 characters).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        db_table = "oc_lettings_site_address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Returns a string representation of the address.
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a letting entity, linked to an address.

    Attributes:
        title (CharField): The title or name of the letting.
        address (OneToOneField): A one-to-one relationship to an Address instance.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = "oc_lettings_site_letting"

    def __str__(self):
        """
        Returns a string representation of the letting.
        """
        return self.title

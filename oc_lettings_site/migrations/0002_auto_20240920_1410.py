# Generated by Django 3.0 on 2024-09-20 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name="letting",
                    name="address",
                ),
                migrations.RemoveField(
                    model_name="profile",
                    name="user",
                ),
                migrations.DeleteModel(
                    name="Address",
                ),
                migrations.DeleteModel(
                    name="Letting",
                ),
                migrations.DeleteModel(
                    name="Profile",
                ),
            ],
            database_operations=[],
        ),
    ]

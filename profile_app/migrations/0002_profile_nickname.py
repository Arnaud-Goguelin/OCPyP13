# Generated by Django 3.0 on 2024-09-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='Bob', max_length=10),
            preserve_default=False,
        ),
    ]

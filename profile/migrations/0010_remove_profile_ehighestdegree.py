# Generated by Django 4.0.3 on 2022-06-14 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0009_profile_erug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ehighestdegree',
        ),
    ]
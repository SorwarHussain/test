# Generated by Django 4.0.3 on 2022-06-13 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0008_profile_ecookingwomen'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='erug',
            field=models.CharField(default='', max_length=300),
        ),
    ]

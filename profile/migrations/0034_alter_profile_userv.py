# Generated by Django 4.0.3 on 2022-08-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0033_delete_post_user_profile_userv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userv',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]

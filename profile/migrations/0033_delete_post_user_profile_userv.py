# Generated by Django 4.0.3 on 2022-08-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0032_rename_user_post_user_userv'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post_User',
        ),
        migrations.AddField(
            model_name='profile',
            name='userv',
            field=models.TextField(default=None),
        ),
    ]

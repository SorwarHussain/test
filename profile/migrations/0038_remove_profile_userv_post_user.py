# Generated by Django 4.0.3 on 2022-08-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0037_alter_profile_userv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='userv',
        ),
        migrations.CreateModel(
            name='Post_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userv', models.TextField(default=None)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile.profile')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0063_video_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.CharField(default='5h 20m', max_length=100),
        ),
    ]

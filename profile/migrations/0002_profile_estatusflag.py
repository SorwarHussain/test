# Generated by Django 4.0.3 on 2022-05-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='estatusFlag',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
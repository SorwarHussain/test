# Generated by Django 4.0.3 on 2023-02-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0050_alter_course_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lectures',
            field=models.IntegerField(default=30),
        ),
    ]
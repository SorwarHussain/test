# Generated by Django 4.0.3 on 2022-11-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0046_course_duration_alter_course_enroled_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(upload_to='static/media/'),
        ),
    ]

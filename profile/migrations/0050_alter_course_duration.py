# Generated by Django 4.0.3 on 2023-02-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0049_course_level_alter_course_course_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(default='10h 20m', max_length=20),
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0020_alter_profile_eclothman_alter_profile_eclothwomen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='esalat',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='esalatstart',
            field=models.CharField(max_length=254),
        ),
    ]

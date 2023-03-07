# Generated by Django 3.2.9 on 2022-03-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0002_delete_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(max_length=700)),
            ],
        ),
    ]

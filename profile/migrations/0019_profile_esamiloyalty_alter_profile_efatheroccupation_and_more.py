# Generated by Django 4.0.3 on 2022-06-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0018_alter_profile_eincome_alter_profile_eoccupation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='esamiLoyalty',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='efatherOccupation',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='emotherOccupation',
            field=models.CharField(max_length=150),
        ),
    ]
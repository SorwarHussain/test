# Generated by Django 4.1.7 on 2023-02-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sadakah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('TransactionID', models.CharField(max_length=100)),
                ('madhom', models.CharField(max_length=100)),
            ],
        ),
    ]

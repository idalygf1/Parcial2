# Generated by Django 4.2 on 2024-10-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Makeup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.CharField(default=True, max_length=202),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=True, max_length=8),
        ),
    ]

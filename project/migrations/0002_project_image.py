# Generated by Django 4.0.3 on 2022-04-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FilePathField(blank=True, path='/img'),
        ),
    ]

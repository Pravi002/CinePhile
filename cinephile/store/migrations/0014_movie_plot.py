# Generated by Django 5.0.3 on 2024-04-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

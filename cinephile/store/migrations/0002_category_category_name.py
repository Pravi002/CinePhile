# Generated by Django 5.0.3 on 2024-04-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-17 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_diary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

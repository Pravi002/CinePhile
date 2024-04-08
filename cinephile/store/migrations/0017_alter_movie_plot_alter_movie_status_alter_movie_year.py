# Generated by Django 5.0.3 on 2024-04-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_movie_cast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('MP', 'MOST-POPULAR'), ('TR', 'TOP-RATED'), ('MA', 'MOST-ANTICIPATED'), ('CS', 'COMING-SOON'), ('EG', 'EVER-GREEN'), ('c', 'CLASSIC')], max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_movie_plot_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('action', 'ACTION'), ('sci-fi', 'SCI-FI'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER'), ('horror', 'HORROR'), ('drama', 'DRAMA'), ('war', 'WAR'), ('historic', 'HISTORIC'), ('documentary', 'DOCUMENTARY'), ('fantasy', 'FANTASY'), ('crime', 'CRIME'), ('sports', 'SPORTS'), ('music', 'MUSIC'), ('romance', 'ROMANCE'), ('animation', 'ANIMATION'), ('slasher', 'SLASHER'), ('adventure', 'ADVENTURE'), ('mystery', 'MYSTERY'), ('survival', 'SURVIVAL'), ('family', 'FAMILY')], max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('MP', 'MOST-POPULAR'), ('TR', 'TOP-RATED'), ('MA', 'MOST-ANTICIPATED'), ('SH', 'SUPER-HIT'), ('CS', 'COMING-SOON'), ('EG', 'EVER-GREEN'), ('cL', 'CLASSIC'), ('BB', 'BLOCK-BUSTER')], max_length=20),
        ),
    ]

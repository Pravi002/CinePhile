# Generated by Django 5.0.3 on 2024-04-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0010_remove_item_category_delete_category_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOVIE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='movie_images')),
                ('genre', models.CharField(choices=[('action', 'ACTION'), ('sci-fi', 'SCI-FI'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER'), ('horror', 'HORROR'), ('drama', 'DRAMA'), ('war', 'WAR'), ('historic', 'HISTORIC'), ('documentary', 'DOCUMENTARY'), ('fantasy', 'FANTASY'), ('crime', 'CRIME'), ('music', 'MUSIC'), ('romance', 'ROMANCE'), ('animation', 'ANIMATION'), ('adventure', 'ADVENTURE'), ('mystery', 'MYSTERY')], max_length=20)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('malayalam', 'MALAYALAM'), ('tamil', 'TAMIL'), ('telugu', 'TELUGU'), ('kannada', 'KANNADA'), ('hindi', 'HINDI'), ('korean', 'KOREAN'), ('french', 'FRENCH'), ('germen', 'GERMEN'), ('chinease', 'CHINEASE')], max_length=20)),
                ('status', models.CharField(choices=[('MP', 'MOST-POPULAR'), ('TR', 'TOP-RATED'), ('MA', 'MOST-ANTICIPATED'), ('CS', 'COMING-SOON')], max_length=20)),
                ('Director', models.CharField(max_length=50)),
                ('cast', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]

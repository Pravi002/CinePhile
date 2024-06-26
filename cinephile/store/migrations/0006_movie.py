# Generated by Django 5.0.3 on 2024-04-02 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_category_discription'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=20)),
                ('duration', models.CharField(max_length=20)),
                ('summary', models.TextField(max_length=700)),
                ('language', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('writter', models.CharField(max_length=50)),
                ('leadrole', models.CharField(max_length=50)),
                ('actor1', models.CharField(max_length=50, null=True)),
                ('actor2', models.CharField(max_length=50, null=True)),
                ('actor3', models.CharField(max_length=50, null=True)),
                ('actor4', models.CharField(max_length=50, null=True)),
                ('actor5', models.CharField(max_length=50, null=True)),
                ('seasons', models.IntegerField(null=True)),
                ('episodes', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]

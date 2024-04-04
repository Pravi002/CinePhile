# Generated by Django 5.0.3 on 2024-04-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_leadrole_item_actor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='actor',
            new_name='writer',
        ),
        migrations.RemoveField(
            model_name='item',
            name='actress',
        ),
        migrations.AddField(
            model_name='item',
            name='cast',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

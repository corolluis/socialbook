# Generated by Django 4.1.7 on 2023-04-25 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_likepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='no_of_lines',
            new_name='no_of_likes',
        ),
    ]

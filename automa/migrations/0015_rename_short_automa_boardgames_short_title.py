# Generated by Django 4.0.3 on 2022-04-05 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automa', '0014_remove_automa_boardgames_short_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='automa_boardgames',
            old_name='short',
            new_name='short_title',
        ),
    ]

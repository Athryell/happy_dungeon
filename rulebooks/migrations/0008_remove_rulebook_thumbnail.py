# Generated by Django 4.0.3 on 2022-04-28 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rulebooks', '0007_remove_rulebook_additional_url_is_official_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rulebook',
            name='thumbnail',
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-27 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_remove_blogpost_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='posted',
            new_name='posted_date',
        ),
    ]

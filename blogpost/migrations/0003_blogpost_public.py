# Generated by Django 2.2.7 on 2019-12-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_remove_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
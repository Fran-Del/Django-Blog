# Generated by Django 4.2 on 2023-05-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_rename_created_date_comment_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

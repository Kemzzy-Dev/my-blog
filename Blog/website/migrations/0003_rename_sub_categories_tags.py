# Generated by Django 4.0.5 on 2022-07-01 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_date_post_created_on_post_sub_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sub_categories',
            new_name='tags',
        ),
    ]

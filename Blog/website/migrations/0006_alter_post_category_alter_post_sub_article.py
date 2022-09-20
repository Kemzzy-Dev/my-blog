# Generated by Django 4.0.5 on 2022-07-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_tag_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('TECH', 'TECH'), ('PYTHON', 'PYTHON'), ('JAVA', 'JAVA'), ('PROGRAMMING', 'PROGRAMMING')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_article',
            field=models.TextField(max_length=255, null=True),
        ),
    ]

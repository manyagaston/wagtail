# Generated by Django 3.2.12 on 2022-02-03 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogspage_sous_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspage',
            name='sous_image',
        ),
    ]

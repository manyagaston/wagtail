# Generated by Django 3.2.12 on 2022-02-01 13:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('titre_et_text_block', wagtail.core.blocks.StructBlock([('titre', wagtail.core.blocks.CharBlock(help_text="titre d'article ", required=True)), ('text', wagtail.core.blocks.CharBlock(help_text='les contenues ', required=True))]))], blank=True, null=True),
        ),
    ]
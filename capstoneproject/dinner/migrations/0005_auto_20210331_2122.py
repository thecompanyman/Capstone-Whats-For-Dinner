# Generated by Django 3.1.7 on 2021-04-01 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0004_auto_20210331_2110'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeIngredient',
            new_name='RecipeIngredients',
        ),
    ]

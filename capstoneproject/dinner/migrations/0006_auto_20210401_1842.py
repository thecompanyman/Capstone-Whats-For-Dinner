# Generated by Django 3.1.7 on 2021-04-02 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0005_auto_20210331_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='link',
            new_name='source',
        ),
    ]
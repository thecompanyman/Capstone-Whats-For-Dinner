# Generated by Django 3.1.7 on 2021-04-09 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsfordinner', '0002_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.TextField(null=True),
        ),
    ]

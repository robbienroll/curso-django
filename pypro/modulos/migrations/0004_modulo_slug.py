# Generated by Django 4.1 on 2022-08-31 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]

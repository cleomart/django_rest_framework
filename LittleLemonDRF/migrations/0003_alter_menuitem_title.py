# Generated by Django 4.2.6 on 2023-11-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0002_alter_menuitem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.SlugField(),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-21 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("healthier", "0003_auto_20200519_1520"),
    ]

    operations = [
        migrations.RenameField(
            model_name="food_item", old_name="Brands", new_name="brands",
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("healthier", "0008_auto_20200521_1444"),
    ]

    operations = [
        migrations.AddField(
            model_name="food_item",
            name="image_nutrition_url",
            field=models.URLField(default=0, max_length=400),
            preserve_default=False,
        ),
    ]

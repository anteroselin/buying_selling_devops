# Generated by Django 2.2.10 on 2020-06-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_auto_20200513_1947"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]

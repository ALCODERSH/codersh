# Generated by Django 4.2 on 2023-04-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="language",
            name="ace_mode",
            field=models.CharField(default="ace/mode/python", max_length=60),
            preserve_default=False,
        ),
    ]

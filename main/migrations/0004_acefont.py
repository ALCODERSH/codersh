# Generated by Django 4.2 on 2023-04-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_acetheme"),
    ]

    operations = [
        migrations.CreateModel(
            name="AceFont",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50)),
            ],
        ),
    ]
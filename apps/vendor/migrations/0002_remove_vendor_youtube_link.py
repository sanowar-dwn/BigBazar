# Generated by Django 4.2.2 on 2023-07-16 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendor",
            name="youtube_link",
        ),
    ]

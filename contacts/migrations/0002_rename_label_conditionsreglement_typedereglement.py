# Generated by Django 4.1.12 on 2024-01-20 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="conditionsreglement",
            old_name="label",
            new_name="typeDeReglement",
        ),
    ]

# Generated by Django 4.1.12 on 2024-01-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0003_alter_client_conditions_reglement_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="adresse",
            field=models.CharField(max_length=255, verbose_name="Adresse"),
        ),
        migrations.AlterField(
            model_name="fournisseur",
            name="adresse",
            field=models.CharField(max_length=255, verbose_name="Adresse"),
        ),
    ]

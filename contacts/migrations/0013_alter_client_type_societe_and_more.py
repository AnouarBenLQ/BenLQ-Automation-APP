# Generated by Django 4.1.12 on 2024-01-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0012_alter_client_raison_sociale_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="type_societe",
            field=models.CharField(
                blank=True,
                choices=[("Societe", "Societé"), ("Particulier", "Particulier")],
                default="Societe",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="fournisseur",
            name="type_societe",
            field=models.CharField(
                blank=True,
                choices=[("Societe", "Societé"), ("Particulier", "Particulier")],
                default="Societe",
                max_length=20,
                null=True,
            ),
        ),
    ]
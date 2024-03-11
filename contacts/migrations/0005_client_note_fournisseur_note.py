# Generated by Django 4.1.12 on 2024-01-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0004_alter_client_adresse_alter_fournisseur_adresse"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="note",
            field=models.TextField(
                default="Pas d'informations", verbose_name="Informations"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fournisseur",
            name="note",
            field=models.TextField(
                default="Pas d'informations", verbose_name="Informations"
            ),
            preserve_default=False,
        ),
    ]
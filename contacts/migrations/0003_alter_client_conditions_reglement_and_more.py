# Generated by Django 4.1.12 on 2024-01-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_rename_label_conditionsreglement_typedereglement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="conditions_reglement",
            field=models.CharField(
                blank=True,
                choices=[
                    ("A_RECEPTION_FACTURE", "À réception de la facture"),
                    ("60_40_A_LA_LIVRAISON", "60% à la commande, 40% à la livraison"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="fournisseur",
            name="conditions_reglement",
            field=models.CharField(
                blank=True,
                choices=[
                    ("A_RECEPTION_FACTURE", "À réception de la facture"),
                    ("60_40_A_LA_LIVRAISON", "60% à la commande, 40% à la livraison"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
# Generated by Django 4.1.12 on 2024-02-12 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productsandservices", "0006_alter_produit_designation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produit",
            name="designation",
            field=models.CharField(
                max_length=255, unique=True, verbose_name="Désignation"
            ),
        ),
        migrations.AlterField(
            model_name="produit",
            name="prix_2",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Prix de Vente-2",
            ),
        ),
        migrations.AlterField(
            model_name="produit",
            name="prix_3",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Prix de Vente-3",
            ),
        ),
        migrations.AlterField(
            model_name="produit",
            name="prix_ttc_2",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Prix de Vente TTC-2",
            ),
        ),
        migrations.AlterField(
            model_name="produit",
            name="prix_ttc_3",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Prix de Vente TTC-3",
            ),
        ),
    ]
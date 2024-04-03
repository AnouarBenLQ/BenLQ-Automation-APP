# Generated by Django 4.1.12 on 2024-02-17 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("productsandservices", "0010_remove_service_pays_dorigine_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pack",
            name="description",
        ),
        migrations.RemoveField(
            model_name="pack",
            name="produits",
        ),
        migrations.CreateModel(
            name="PackProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "pack",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productsandservices.pack",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productsandservices.produit",
                    ),
                ),
            ],
        ),
    ]

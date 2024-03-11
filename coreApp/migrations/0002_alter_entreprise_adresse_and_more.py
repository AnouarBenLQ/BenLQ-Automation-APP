# Generated by Django 4.1.12 on 2024-01-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coreApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entreprise",
            name="adresse",
            field=models.TextField(blank=True, null=True, verbose_name="Adresse"),
        ),
        migrations.AlterField(
            model_name="entreprise",
            name="code_postal",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Code postal"
            ),
        ),
        migrations.AlterField(
            model_name="entreprise",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Adresse email"
            ),
        ),
        migrations.AlterField(
            model_name="entreprise",
            name="informations_fiscales",
            field=models.TextField(
                blank=True, null=True, verbose_name="Informations fiscales"
            ),
        ),
        migrations.AlterField(
            model_name="entreprise",
            name="site_web",
            field=models.URLField(blank=True, null=True, verbose_name="Site Web"),
        ),
        migrations.AlterField(
            model_name="entreprise",
            name="telephone",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Téléphone"
            ),
        ),
        migrations.AlterField(
            model_name="entreprise",
            name="ville",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Ville"
            ),
        ),
    ]
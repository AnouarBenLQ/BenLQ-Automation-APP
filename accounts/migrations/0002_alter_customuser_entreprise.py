# Generated by Django 4.1.12 on 2024-01-06 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("coreApp", "0001_initial"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="entreprise",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="comptables",
                to="coreApp.entreprise",
                verbose_name="Entreprise",
            ),
        ),
    ]

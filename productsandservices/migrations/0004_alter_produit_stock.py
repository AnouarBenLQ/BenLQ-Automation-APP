# Generated by Django 5.0.1 on 2024-02-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsandservices', '0003_alter_produit_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='stock',
            field=models.PositiveIntegerField(default=1, verbose_name='Quantité sur stock'),
        ),
    ]
# Generated by Django 5.0 on 2024-03-28 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productsandservices', '0018_alter_produit_prix_1_alter_produit_prix_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remise',
            old_name='type',
            new_name='type_remise',
        ),
    ]

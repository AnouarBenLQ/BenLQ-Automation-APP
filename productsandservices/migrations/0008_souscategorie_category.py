# Generated by Django 5.0.1 on 2024-02-14 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsandservices', '0007_alter_produit_designation_alter_produit_prix_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='souscategorie',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productsandservices.categorie'),
            preserve_default=False,
        ),
    ]

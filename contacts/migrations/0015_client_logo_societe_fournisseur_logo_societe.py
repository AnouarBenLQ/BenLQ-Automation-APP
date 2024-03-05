# Generated by Django 5.0.1 on 2024-01-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_alter_client_type_societe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='logo_societe',
            field=models.ImageField(blank=True, null=True, upload_to='contacts/logos/', verbose_name='Logo Contact'),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='logo_societe',
            field=models.ImageField(blank=True, null=True, upload_to='contacts/logos/', verbose_name='Logo Contact'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0009_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='totalCde',
            field=models.FloatField(editable=False),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-04 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vegetta777', '0003_articulus_clientes_pedidos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulus',
            old_name='precin',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='tfno',
            new_name='telefonoo',
        ),
        migrations.RenameField(
            model_name='pedidos',
            old_name='numern',
            new_name='numero',
        ),
    ]

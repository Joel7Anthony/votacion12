# Generated by Django 4.0.6 on 2022-08-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetta777', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='djmariio',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-23 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_camiseta_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='camiseta',
            name='descripcion',
            field=models.TextField(default='SOME STRING'),
        ),
    ]

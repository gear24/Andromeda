# Generated by Django 4.2.1 on 2023-12-08 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andro', '0006_alter_detallescompra_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallescompra',
            name='compra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='andro.compra'),
        ),
    ]

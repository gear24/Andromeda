# Generated by Django 4.2.1 on 2023-12-08 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andro', '0002_compra_contacto_1_compra_contacto_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallescompra',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='andro.compra'),
        ),
        migrations.AlterField(
            model_name='detallescompra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='andro.producto'),
        ),
    ]

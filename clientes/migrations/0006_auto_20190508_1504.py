# Generated by Django 2.2 on 2019-05-08 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Person'),
        ),
    ]

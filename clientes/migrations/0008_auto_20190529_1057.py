# Generated by Django 2.2 on 2019-05-29 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20190508_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='nfe_emitida',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(verbose_name='Biografia'),
        ),
        migrations.AlterField(
            model_name='person',
            name='doc',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Documento', verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salário'),
        ),
    ]

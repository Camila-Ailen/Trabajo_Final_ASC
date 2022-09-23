# Generated by Django 4.1.1 on 2022-09-23 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaYHora', models.DateTimeField(auto_now_add=True)),
                ('montoDePago', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nroComprobante', models.PositiveIntegerField(null=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('id_tipoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pago.tipopago')),
            ],
        ),
    ]
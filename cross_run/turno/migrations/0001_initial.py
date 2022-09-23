# Generated by Django 4.1.1 on 2022-09-23 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cuotaClientesMaximo', models.PositiveIntegerField()),
                ('cuotaClientesMinimo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TurnoTemporal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHoy', models.DateField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('id_turno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turno.turno')),
            ],
        ),
    ]
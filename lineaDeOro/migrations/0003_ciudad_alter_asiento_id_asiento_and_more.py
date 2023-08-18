# Generated by Django 4.2.2 on 2023-08-17 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lineaDeOro', '0002_autobus_chofer_origen_viaje_asiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ciudad', models.CharField(max_length=100)),
                ('url_imagen', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='asiento',
            name='id_asiento',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='autobus',
            name='id_autobus',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chofer',
            name='id_chofer',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='destino',
            name='id_destino',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='origen',
            name='id_origen',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='id_viaje',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='destino',
            name='ciudad_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lineaDeOro.ciudad'),
        ),
        migrations.AlterField(
            model_name='origen',
            name='ciudad_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lineaDeOro.ciudad'),
        ),
    ]
# Generated by Django 3.2.8 on 2022-04-13 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_measurements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='modified_at',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurements',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_m', to='measurement.sensor'),
        ),
    ]

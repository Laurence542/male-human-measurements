# Generated by Django 4.2 on 2023-04-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_waistmeasurement'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaleMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('age', models.IntegerField()),
                ('weight', models.FloatField()),
                ('waist', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='WaistMeasurement',
        ),
    ]

# Generated by Django 4.2 on 2023-04-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaistMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waist_measurement', models.FloatField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-04-21 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_malemeasurement_delete_waistmeasurement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MaleMeasurement',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]

# Generated by Django 4.2 on 2023-04-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_malemeasurement_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malemeasurement',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='malemeasurement',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='malemeasurement',
            name='waist',
            field=models.IntegerField(),
        ),
    ]

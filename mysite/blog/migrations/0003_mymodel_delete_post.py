# Generated by Django 4.2 on 2023-04-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

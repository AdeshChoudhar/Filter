# Generated by Django 3.2 on 2021-04-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0002_auto_20210405_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1 on 2022-09-18 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_type_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['order', 'title'], 'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.AlterModelTable(
            name='type',
            table='type',
        ),
    ]
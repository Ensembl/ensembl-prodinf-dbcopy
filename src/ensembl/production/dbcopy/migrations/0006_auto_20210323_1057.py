# Generated by Django 3.1.7 on 2021-03-23 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensembl_dbcopy', '0005_targethostgroup'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='group',
            table='host_group',
        ),
    ]

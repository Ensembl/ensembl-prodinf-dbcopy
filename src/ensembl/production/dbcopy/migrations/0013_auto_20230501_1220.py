# Generated by Django 3.2.17 on 2023-05-01 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensembl_dbcopy', '0012_dcserver_host_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='_ro_user',
            field=models.CharField(max_length=32, db_column='ro_user', null=True),
        ),
        migrations.AlterField(
            model_name='requestjob',
            name='src_host',
            field=models.TextField(max_length=2048, validators=[django.core.validators.RegexValidator(message='Source Host should be: host:port', regex='^[\\w\\.-]+:[0-9]{4}')], verbose_name='Source Host'),
        ),
    ]

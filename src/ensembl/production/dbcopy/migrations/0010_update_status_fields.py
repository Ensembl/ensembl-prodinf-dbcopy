# Generated by Django 3.2.9 on 2021-11-11 17:03

import django.core.validators
from django.db import migrations, models
import ensembl.production.djcore.forms
import ensembl.production.djcore.models


class Migration(migrations.Migration):

    dependencies = [
        ('ensembl_dbcopy', '0009_rename_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='host',
            options={'ordering': ('name',), 'verbose_name': 'Host'},
        ),
        migrations.AlterModelOptions(
            name='hostgroup',
            options={'verbose_name': 'Host HostGroup'},
        ),
        migrations.AlterModelOptions(
            name='requestjob',
            options={'ordering': ('-request_date',), 'verbose_name': 'Copy job', 'verbose_name_plural': 'Copy jobs'},
        ),
        migrations.AddField(
            model_name='requestjob',
            name='completed',
            field=models.IntegerField(blank=True, editable=False, null=True, verbose_name='Transfers completed'),
        ),
        migrations.AddField(
            model_name='requestjob',
            name='expected',
            field=models.IntegerField(blank=True, editable=False, null=True, verbose_name='Expected to transfer'),
        ),
        migrations.AddField(
            model_name='requestjob',
            name='overall_status',
            field=models.CharField(blank=True, editable=False, max_length=48, null=True, verbose_name='Overall Status'),
        ),
        migrations.AlterField(
            model_name='hostgroup',
            name='group_name',
            field=models.CharField(max_length=80, verbose_name='User HostGroup'),
        ),
        migrations.AlterField(
            model_name='requestjob',
            name='email_list',
            field=models.TextField(blank=True, max_length=2048, null=True, validators=[ensembl.production.djcore.forms.EmailListFieldValidator(message='Email list should contain one or more comma separated valid email addresses.')], verbose_name='Notify Email(s)'),
        ),
        migrations.AlterField(
            model_name='requestjob',
            name='src_host',
            field=models.TextField(max_length=2048, validators=[django.core.validators.RegexValidator(message='Source Host should be: host:port', regex='^[\\w-]+:[0-9]{4}')], verbose_name='Source Host'),
        ),
        migrations.AlterField(
            model_name='requestjob',
            name='src_incl_db',
            field=ensembl.production.djcore.models.NullTextField(blank=True, default='%', max_length=2048, null=True, verbose_name='Included Db(s)'),
        ),
        migrations.AlterField(
            model_name='requestjob',
            name='status',
            field=models.CharField(blank=True, editable=False, max_length=40, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='requestjob',
            name='tgt_host',
            field=models.TextField(max_length=2048, validators=[ensembl.production.djcore.forms.ListFieldRegexValidator(message='Target Hosts should be formatted like this host:port or host1:port1,host2:port2', regex='^[\\w-]+:[0-9]{4}')], verbose_name='Target Host(s)'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-17 21:59

from django.db import migrations, models
import django.db.models.deletion
import ensembl.production.djcore.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dbs2Exclude',
            fields=[
                ('table_schema', models.CharField(db_column='TABLE_SCHEMA', max_length=64, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'dbs_2_exclude',
            },
        ),
        migrations.CreateModel(
            name='DebugLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(blank=True, max_length=128, null=True)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('function', models.CharField(blank=True, max_length=128, null=True)),
                ('value', models.TextField(blank=True, max_length=8192, null=True)),
            ],
            options={
                'db_table': 'debug_log',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('auto_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('port', models.IntegerField()),
                ('mysql_user', models.CharField(max_length=64)),
                ('virtual_machine', models.CharField(blank=True, max_length=255, null=True)),
                ('mysqld_file_owner', models.CharField(blank=True, max_length=128, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Host',
                'db_table': 'host',
                'unique_together': {('name', 'port')},
            },
        ),
        migrations.CreateModel(
            name='RequestJob',
            fields=[
                ('job_id', models.CharField(default=uuid.uuid1, editable=False, max_length=128, primary_key=True, serialize=False)),
                ('src_host', models.TextField(max_length=2048)),
                ('src_incl_db', ensembl.production.djcore.models.NullTextField(blank=True, max_length=2048, null=True)),
                ('src_skip_db', ensembl.production.djcore.models.NullTextField(blank=True, max_length=2048, null=True)),
                ('src_incl_tables', ensembl.production.djcore.models.NullTextField(blank=True, max_length=2048, null=True)),
                ('src_skip_tables', ensembl.production.djcore.models.NullTextField(blank=True, max_length=2048, null=True)),
                ('tgt_host', models.TextField(max_length=2048)),
                ('tgt_db_name', ensembl.production.djcore.models.NullTextField(blank=True, max_length=2048, null=True)),
                ('tgt_directory', ensembl.production.djcore.models.NullTextField(blank=True, max_length=2048, null=True)),
                ('skip_optimize', models.BooleanField(default=False)),
                ('wipe_target', models.BooleanField(default=False)),
                ('convert_innodb', models.BooleanField(default=False)),
                ('dry_run', models.BooleanField(default=False)),
                ('email_list', models.TextField(blank=True, max_length=2048, null=True)),
                ('start_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('end_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('user', models.CharField(blank=True, max_length=64, null=True)),
                ('status', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Copy job',
                'verbose_name_plural': 'Copy jobs',
                'db_table': 'request_job',
            },
        ),
        migrations.CreateModel(
            name='TargetHostGroup',
            fields=[
                ('target_group_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('target_group_name', models.CharField(max_length=80, unique=True, verbose_name='Hosts Group')),
                ('target_host', models.ManyToManyField(to='ensembl_dbcopy.Host')),
            ],
            options={
                'verbose_name': 'Hosts Target Group',
                'db_table': 'target_host_group',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=80, verbose_name='User Group')),
                ('host_id', models.ForeignKey(db_column='auto_id', on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='ensembl_dbcopy.host')),
            ],
            options={
                'verbose_name': 'Host Group',
            },
        ),
        migrations.CreateModel(
            name='TransferLog',
            fields=[
                ('auto_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tgt_host', models.CharField(editable=False, max_length=512)),
                ('table_schema', models.CharField(db_column='TABLE_SCHEMA', editable=False, max_length=64)),
                ('table_name', models.CharField(db_column='TABLE_NAME', editable=False, max_length=64)),
                ('renamed_table_schema', models.CharField(editable=False, max_length=64)),
                ('target_directory', models.TextField(blank=True, editable=False, max_length=2048, null=True)),
                ('start_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('end_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('size', models.BigIntegerField(blank=True, editable=False, null=True)),
                ('retries', models.IntegerField(blank=True, editable=False, null=True)),
                ('message', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('job_id', models.ForeignKey(db_column='job_id', on_delete=django.db.models.deletion.CASCADE, related_name='transfer_logs', to='ensembl_dbcopy.requestjob')),
            ],
            options={
                'verbose_name': 'TransferLog',
                'db_table': 'transfer_log',
                'unique_together': {('job_id', 'tgt_host', 'table_schema', 'table_name')},
            },
        ),
    ]

# Generated by Django 2.2.13 on 2020-11-19 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbcopy', '0002_adding_request_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbs2exclude',
            name='id',
        ),
        migrations.AddField(
            model_name='requestjob',
            name='dry_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dbs2exclude',
            name='table_schema',
            field=models.CharField(db_column='TABLE_SCHEMA', max_length=64, primary_key=True, serialize=False),
        ),
    ]
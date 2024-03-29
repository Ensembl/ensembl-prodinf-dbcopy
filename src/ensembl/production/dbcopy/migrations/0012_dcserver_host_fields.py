# Generated by Django 3.2.15 on 2022-09-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensembl_dbcopy', '0011_alter_requestjob_src_incl_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='dc_allowed_server',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='host',
            name='dc_config_profile',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='dc_server_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='requestjob',
            name='skip_optimize',
            field=models.BooleanField(default=False, verbose_name='Skip Target Optimize'),
        ),
        migrations.AlterField(
            model_name='requestjob',
            name='src_incl_db',
            field=models.TextField(max_length=2048, verbose_name='Included Db(s)'),
        ),
    ]

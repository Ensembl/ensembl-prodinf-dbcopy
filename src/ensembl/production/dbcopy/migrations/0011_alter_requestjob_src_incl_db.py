# Generated by Django 3.2.10 on 2022-01-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensembl_dbcopy', '0010_update_status_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestjob',
            name='src_incl_db',
            field=models.TextField(default='%', help_text="Put '%' to copy all the server content (use with caution!)", max_length=2048, verbose_name='Included Db(s)'),
            preserve_default=False,
        ),
    ]
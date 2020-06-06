# Generated by Django 2.2.6 on 2019-11-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ioms', '0003_auto_20191101_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iom',
            options={'ordering': ('speciality', 'subject'), 'verbose_name': 'IOM手册', 'verbose_name_plural': 'IOM手册'},
        ),
        migrations.AlterField(
            model_name='iom',
            name='equipment',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
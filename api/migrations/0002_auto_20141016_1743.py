# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'application',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='server',
            name='ipaddress',
            field=models.IPAddressField(verbose_name=b'IP'),
        ),
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]

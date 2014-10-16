# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('system_operational', models.CharField(max_length=30)),
                ('ipaddress', models.IPAddressField()),
            ],
            options={
                'db_table': 'server',
            },
            bases=(models.Model,),
        ),
    ]

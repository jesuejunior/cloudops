# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141016_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='applications',
            field=models.ManyToManyField(related_name=b'applications', null=True, to='api.Application', db_table=b'server_has_applications', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(unique=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='server',
            name='ipaddress',
            field=models.IPAddressField(unique=True, verbose_name=b'IP'),
        ),
    ]

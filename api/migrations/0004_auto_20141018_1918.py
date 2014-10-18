# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20141017_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='applications',
            field=models.ManyToManyField(related_name=b'servers', db_table=b'server_has_applications', to=b'api.Application'),
        ),
    ]

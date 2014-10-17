# -*- coding: utf-8 -*-
from django.db import models
from api.models.application import Application
from common.helptools import format_unicode


class Server(models.Model):

    name = models.CharField(max_length=60)
    system_operational = models.CharField(max_length=30)
    ipaddress = models.IPAddressField(verbose_name='IP', unique=True)
    applications = models.ManyToManyField(Application, related_name='applications', db_table='server_has_applications')

    class Meta:
        db_table = 'server'

    def __unicode__(self):
        return format_unicode(self.name)
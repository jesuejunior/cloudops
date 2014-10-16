from django.db import models
from api.models.application import Application


class Server(models.Model):

    name = models.CharField(max_length=60)
    system_operational = models.CharField( max_length=30)
    ipaddress = models.IPAddressField(verbose_name='IP')
    # applications = models.ManyToManyField(Application, related_name='applications', db_table='server_has_applications', null=True, blank=True)

    class Meta:
        db_table = 'server'

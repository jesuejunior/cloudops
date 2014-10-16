from django.db import models


class Server(models.Model):

    name = models.CharField(max_length=60)
    system_operational = models.CharField( max_length=30)
    ipaddress = models.IPAddressField(verbose_name='IP')


    class Meta:
        db_table = 'server'

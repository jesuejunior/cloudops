from django.db import models
from common.helptools import format_unicode


class Application(models.Model):

    name = models.CharField(max_length=60, unique=True)
    description = models.TextField()

    class Meta:
        db_table = 'application'

    def __unicode__(self):
        return format_unicode(self.name)

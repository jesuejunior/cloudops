from django.db import models


class Application(models.Model):

    name = models.CharField(max_length=60, unique=True)
    description = models.TextField()

    class Meta:
        db_table = 'application'

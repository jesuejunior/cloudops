from django.db import models

from api.models import Server
from common.testtools import TestCase


class ServerTest(TestCase):

        def test_name(self):
            server = Server._meta.get_field_by_name('name')[0]
            assert server.__class__ == models.CharField
            assert server.max_length == 60
            assert not server.null
            assert not server.blank

        def test_system_operational(self):
            server = Server._meta.get_field_by_name('system_operational')[0]
            assert server.__class__ == models.CharField
            assert server.max_length == 30
            assert not server.null
            assert not server.blank

        def test_ipaddress(self):
            server = Server._meta.get_field_by_name('ipaddress')[0]
            assert server.__class__ == models.IPAddressField
            assert server.unique
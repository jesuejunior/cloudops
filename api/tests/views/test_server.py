import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import pytest
from api.models.server import Server
from common.testtools import TestCase


@pytest.mark.django_db
class ServerTest(TestCase):
    def setUp(self):
        self.server_data = {
            'name': 'test1',
            'system_operational': 'Ubuntu',
            'ipaddress': '192.168.1.2'
        }

        self.user = User.objects.create_user(username="testops", email='testops@google.com')
        self.user.set_password('123456')
        self.user.save()
        self.data = self.client.post(reverse('auth'), {'username': 'testops', 'password': '123456'})
        self.token = json.loads(self.data.content).get('token')

    # def tearDown(self):
        # User.objects.all().delete()
        # Server.objects.all().delete()

    def test_list_all_servers(self):
        for i in [1,2,3]:
            Server.objects.create(name='test-{0}'.format(i), ipaddress='192.168.1.{0}'.format(i), system_operational='ubuntu')

        assert Server.objects.count() == 3

        res = self.client.get(reverse('server-list'), HTTP_AUTHORIZATION='Token {0}'.format(self.token))
        counter = json.loads(res.content).get('count')
        assert counter == 3

    def test_create_server_ok(self):
        """
            Teste para criar um server corretamente
        """
        res = self.client.post(reverse('server-new'), self.server_data, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )

        assert res.status_code == 201

        server = Server.objects.get(name='test1')

        assert server.name == self.server_data['name']
        assert server.ipaddress == self.server_data['ipaddress']
        assert server.system_operational == self.server_data['system_operational']



    def test_create_same_server_twice(self):
        self.fail()

    def test_update_server_info(self):
        self.fail()

    def test_delete_server_exist(self):
        self.fail()

    def test_try_delete_server_not_exist(self):
        self.fail()

    def test_update_server_aplications(self):
        self.fail()


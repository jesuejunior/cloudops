# -*- coding: utf-8 -*-
import json

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import pytest
from api.models import Application

from api.models.server import Server
from common.testtools import TestCase


@pytest.mark.django_db
class ServerTest(TestCase):
    def setUp(self):
        self.post = {
            'name': 'cloudops',
            'system_operational': 'Ubuntu',
            'ipaddress': '192.168.1.2'
        }
        for i in [1,2]:
            Application.objects.create(name='gunicorn-{0}'.format(i), description='http server {0}'.format(i))

        self.user = User.objects.create_user(username="testops", email='testops@google.com')
        self.user.set_password('123456')
        self.user.save()
        self.data = self.client.post(reverse('auth'), {'username': 'testops', 'password': '123456'})
        self.token = json.loads(self.data.content).get('token')


    def tearDown(self):
        # User.objects.all().delete()
        Server.objects.all().delete()

    def test_list_all_servers(self):
        for i in [1,2,3]:
            Server.objects.create(name='test-{0}'.format(i), ipaddress='192.168.1.{0}'.format(i), system_operational='ubuntu')

        assert Server.objects.count() == 3

        res = self.client.get(reverse('server-list'), HTTP_AUTHORIZATION='Token {0}'.format(self.token))
        counter = json.loads(res.content).get('count')
        assert counter == 3

    def test_create_server_ok(self):
        u"""
            Teste para criar um server corretamente
        """
        res = self.client.post(reverse('server-new'), data=json.dumps(self.post), content_type='application/json',
                               HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 201

        server = Server.objects.get(name='cloudops')
        assert server.name == self.post['name']
        assert server.ipaddress == self.post['ipaddress']
        assert server.system_operational == self.post['system_operational']

    def test_create_server_with_apps(self):
        u"""
            Teste para criar um servidor com aplicações
        """
        self.post['applications'] = [1,2]

        res = self.client.post(reverse('server-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 201

        server = Server.objects.get(name='cloudops', )
        assert server.name == self.post['name']
        assert server.ipaddress == self.post['ipaddress']
        assert server.system_operational == self.post['system_operational']
        assert server.applications.values_list('id', flat=True), self.post['applications']


    def test_create_server_wrong_post(self):
        """
            Teste para criar um servidor com dados errados
        """
        self.post['name'] = ''
        res = self.client.post(reverse('server-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 400

        data = json.loads(res.content)
        assert data['name'] == ['This field is required.']


    def test_create_same_server_twice(self):
        u"""
            Testando a criação da mesmo servidor
        """
        res = self.client.post(reverse('server-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 201

        res = self.client.post(reverse('server-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 400

        assert Server.objects.count() == 1





    def test_update_server_info_patch(self):
        server = Server.objects.create(**self.post)

        server_db = Server.objects.get(id=1)
        assert server_db.name == 'cloudops'
        assert server_db.ipaddress == '192.168.1.2'
        assert server_db.system_operational == 'Ubuntu'

        self.post['ipaddress'] = '192.168.1.223'
        res = self.client.patch(reverse('server-edit', kwargs={'pk': server.id}), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 200

        server_res = Server.objects.get(id=1)
        assert server_res.name == 'cloudops'
        assert server_res.ipaddress == '192.168.1.223'
        assert server_res.system_operational == 'Ubuntu'


    def test_update_server_info_put(self):
        server = Server.objects.create(**self.post)

        server_db = Server.objects.get(id=1)
        assert server_db.name == 'cloudops'
        assert server_db.ipaddress == '192.168.1.2'
        assert server_db.system_operational == 'Ubuntu'

        self.post['ipaddress'] = '192.168.1.223'
        res = self.client.put(reverse('server-edit', kwargs={'pk': server.id}), data=json.dumps(self.post),
                              content_type='application/json', HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 200

        server_res = Server.objects.get(id=1)
        assert server_res.name == 'cloudops'
        assert server_res.ipaddress == '192.168.1.223'
        assert server_res.system_operational == 'Ubuntu'

    def test_delete_server_exist(self):
        server = Server.objects.create(**self.post)

        res = self.client.delete(reverse('server-delete', kwargs={'pk': server.id}), HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 204
        assert Server.objects.count() == 0

    def test_try_delete_server_not_exist(self):
        res = self.client.delete(reverse('server-delete', kwargs={'pk': 4}), HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 404


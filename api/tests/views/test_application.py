# -*- coding: utf-8 -*-
import json

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import pytest

from api.models import Application
from common.testtools import TestCase


@pytest.mark.django_db
class ApplicationTest(TestCase):
    def setUp(self):
        self.post = {
            'name': 'Nginx',
            'description': 'Webserver',
        }

        self.user = User.objects.create_user(username="testops", email='testops@google.com')
        self.user.set_password('123456')
        self.user.save()
        self.data = self.client.post(reverse('auth'), {'username': 'testops', 'password': '123456'})
        self.token = json.loads(self.data.content).get('token')

    def tearDown(self):
        # User.objects.all().delete()
        Application.objects.all().delete()

    def test_list_all_applications(self):
        for i in [1,2,3]:
            Application.objects.create(name='test-{0}'.format(i), description='abc teste {0}'.format(i))

        assert Application.objects.count() == 3

        res = self.client.get(reverse('application-list'), HTTP_AUTHORIZATION='Token {0}'.format(self.token))
        counter = json.loads(res.content).get('count')
        assert counter == 3

    def test_create_application_ok(self):
        """
            Teste para criar uma aplicacao corretamente
        """
        res = self.client.post(reverse('application-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )

        assert res.status_code == 201

        application = Application.objects.get(name='Nginx')

        assert application.name == self.post['name']
        assert application.description == self.post['description']

    def test_create_application_wrong_post(self):
        """
            Teste para criar uma aplicacao com dados errados
        """
        self.post['description'] = ''
        res = self.client.post(reverse('application-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )

        assert res.status_code == 400

        data = json.loads(res.content)
        assert data['description'] == ['This field is required.']


    def test_create_same_application_twice(self):
        u"""
            Testando a criacao da mesma aplicação
        """
        res = self.client.post(reverse('application-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 201

        res = self.client.post(reverse('application-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 400

        assert Application.objects.count() == 1

    def test_update_application_info_patch(self):
        app = Application.objects.create(**self.post)

        app_db = Application.objects.get(id=1)
        assert app_db.name == 'Nginx'
        assert app_db.description == 'Webserver'

        self.post['description'] = 'Super proxy server'
        res = self.client.patch(reverse('application-edit', kwargs={'pk': app.id}), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 200

        app_res = Application.objects.get(id=1)
        assert app_res.name == 'Nginx'
        assert app_res.description == 'Super proxy server'


    def test_update_application_info_put(self):
        app = Application.objects.create(**self.post)

        app_db = Application.objects.get(id=1)
        assert app_db.name == 'Nginx'
        assert app_db.description == 'Webserver'

        self.post['description'] = 'Super proxy server'
        res = self.client.put(reverse('application-edit', kwargs={'pk': app.id}), data=json.dumps(self.post),
                              content_type='application/json', HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 200

        app_res = Application.objects.get(id=1)
        assert app_res.name == 'Nginx'
        assert app_res.description == 'Super proxy server'

    def test_delete_application_exist(self):
        app = Application.objects.create(**self.post)

        res = self.client.delete(reverse('application-delete', kwargs={'pk': app.id}), HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 204
        assert Application.objects.count() == 0


    def test_try_delete_application_not_exist(self):
        res = self.client.delete(reverse('application-delete', kwargs={'pk': 4}), HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 404

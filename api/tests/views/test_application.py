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

    # def tearDown(self):
        # User.objects.all().delete()
        # Server.objects.all().delete()

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


    def test_create_same_application_twice(self):
        """
            Testando a criacao da mesma aplicacao
        """
        res = self.client.post(reverse('application-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 201

        res = self.client.post(reverse('application-new'), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )
        assert res.status_code == 400

        assert Application.objects.count() == 1

    def test_update_application_info(self):
        app = Application.objects.create(**self.post)

        self.post['description'] = 'Super proxy server'
        res = self.client.put(reverse('application-edit', {'pk': app.id}), self.post, HTTP_AUTHORIZATION='Token {0}'.format(self.token) )

        assert res.status_code == 200

    def test_delete_application_exist(self):
        self.fail()

    def test_try_delete_application_not_exist(self):
        self.fail()


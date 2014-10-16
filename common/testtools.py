__author__ = 'jesuejunior'
#coding:utf-8
from urlparse import urlparse
from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import TestCase as DjangoTestCase
from django.test import Client
from django.conf import settings
from django.contrib.auth.models import User
from django.test.client import MULTIPART_CONTENT, FakePayload


class MockedResponse(object):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

class ReverserClient(Client):
    def _resolve(self, path, kwargs):
        """
        Helper method to enable automatic resolution of named urls.

        def test_method(self):
            self.get('namespace:name', args=[1])
            self.get('/hardcoded/url/')
            self.post('namespace:name', args=[2], data={'key': value})
            self.post(('namespace:name', [2]), {'key': value})
            self.post('namespace:name', {'key': value}, args=[2])
            self.post('/hardcoded/url/', {'key': value})

        """
        # If path is a tuple, pass it right to reverse
        if isinstance(path, (tuple, list)):
            return reverse(path)

        # extract reverse's args if present in kwargs.
        args = kwargs.pop('args', [])

        try:
            return reverse(path, args=args)
        except NoReverseMatch:
            return path

    def get(self, path, *args, **kwargs):
        resolved_path = self._resolve(path, kwargs)
        return super(ReverserClient, self).get(resolved_path, *args, **kwargs)

    def post(self, path, *args, **kwargs):
        resolved_path = self._resolve(path, kwargs)
        return super(ReverserClient, self).post(resolved_path, *args, **kwargs)

    def patch(self, path, data={}, content_type=MULTIPART_CONTENT,
             follow=False, **extra):
        """
        Requests a response from the server using POST.
        """
        response = self.make_patch(path, data=data, content_type=content_type, **extra)
        if follow:
            response = self._handle_redirects(response, **extra)
        return response

    def make_patch(self, path, data={}, content_type=MULTIPART_CONTENT,
         **extra):
        "Construct a PATCH request."

        patch_data = self._encode_data(data, content_type)

        parsed = urlparse(path)
        r = {
            'CONTENT_LENGTH': len(patch_data),
            'CONTENT_TYPE':   content_type,
            'PATH_INFO':      self._get_path(parsed),
            'QUERY_STRING':   parsed[4],
            'REQUEST_METHOD': 'PATCH',
            'wsgi.input':     FakePayload(patch_data),
        }
        r.update(extra)
        return self.request(**r)


class TestCase(DjangoTestCase):
    client_class = ReverserClient

    def assertCorrectTemplateForView(self, url, template_name, method='get', data=None):
        response = self.client.get(url, data=data or {})
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template_name)

    def assertQuerySetEqual(self, qs1, qs2, *args, **kwargs):
        self.assertEqual(list(qs1), list(qs2), *args, **kwargs)

    def assertRecipients(self, email, recipients):
        email_recipients = sorted(email.recipients())
        self.assertEqual(email_recipients, sorted(recipients))

    def assertNotRecipient(self, email, recipient):
        email_recipients = sorted(email.recipients())
        self.assertNotIn(recipient, email_recipients)

    def assertLoginRequired(self, url, method='get', data=None):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        login_url = settings.LOGIN_URL
        self.assertTrue(login_url in response['Location'])

    def assertChoiceFieldOptions(self, expected_choices, form, field_name):
        expected_choices = list(expected_choices)
        self.assertEqual(expected_choices, form.fields[field_name].choices)

    def log_user(self, username='username', email='email@example.com', password='passwd'):
        user = User.objects.create_user(username=username, email=email, password=password)
        self.client.login(username=username, password=password)
import json
import unittest
from django.test import RequestFactory
from common.decorators import is_ajax

__author__ = 'jesuejunior'

@is_ajax
def my_view(request):
    return {"message": "It's ajax"}


class IsAjaxDecoratorTest(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_request_not_ajax(self):

        request = self.factory.get('/my-view/')
        response = my_view(request)
        self.assertEquals(response.content, '')

    def test_is_ajax_ok(self):
        request = self.factory.get('/my-view/',  HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = my_view(request)
        content = json.loads(response.content)
        self.assertEquals(content, {"message": "It's ajax"})
from django.db import models

from api.models import Application
from common.testtools import TestCase


class ApplicationTest(TestCase):

        def test_name(self):
            app = Application._meta.get_field_by_name('name')[0]
            assert app.__class__ == models.CharField
            assert app.max_length == 60
            assert not app.null
            assert not app.blank
            assert app.unique

        def test_description(self):
            app = Application._meta.get_field_by_name('description')[0]
            assert app.__class__ == models.TextField
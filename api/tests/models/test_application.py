from django.db import models

from api.models import Application
from common.testtools import TestCase


class ApplicationTest(TestCase):

        def test_name(self):
            app = Application._meta.get_field_by_name('name')[0]
            self.assertEquals(app.__class__, models.CharField)
            self.assertEquals(app.max_length, 60)
            self.assertTrue(app.null)
            self.assertTrue(app.blank)

        def test_description(self):
            app = Application._meta.get_field_by_name('description')[0]
            self.assertEquals(app.__class__, models.TextField)
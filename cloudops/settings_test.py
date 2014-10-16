# -*- coding: utf-8 -*-
from cloudops.settings import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory',
}

# SOUTH_TESTS_MIGRATE = False

TEST_RUNNER = 'juxd.JUXDTestSuiteRunner'
JUXD_FILENAME = 'junit.opsworks.xml'

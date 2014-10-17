from django.utils.encoding import smart_unicode


def format_unicode(*args):
    return u' - '.join([smart_unicode(i) for i in args])

from json import dumps
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseBadRequest

__author__ = 'jesuejunior'

def is_ajax(method_to_decorate):
    def continue_or_bad_request(request, *args, **kwargs):
        if request.is_ajax():
            response = method_to_decorate(request, *args, **kwargs)
            #HttpResponse* herdam de HttpResponse, sendo assim, instancias da classe pai
            if isinstance(response, HttpResponse):
                return response
            else:
                return HttpResponse(dumps(response, cls=DjangoJSONEncoder), content_type="application/json")
        else:
            return HttpResponseBadRequest()
    return continue_or_bad_request

import pico.server
from pico import PicoError

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

pico.server.DEBUG = settings.DEBUG


@csrf_exempt
def index(request):
    params = {}
    params.update(request.GET.dict())
    params.update(request.POST.dict())
    path = '/' + request.path.split('/pico/')[-1]
    try:
        pico_response = pico.server.handle_api_v2(path, params, request)
    except PicoError, e:
        pico_response = e.response
    except Exception, e:
        pico_response = pico.server.generate_exception_report(e, path, params)
    code, reason = pico_response.status.split(' ', 1)
    response = HttpResponse(pico_response.output,
                            status=int(code),
                            reason=reason)
    for key, header in pico_response.headers:
        response[key] = header
    return response


def picojs(request):
    f = open(pico.server.pico_path + 'client.js')
    return HttpResponse(f.read(), mimetype='application/javascript')

import pico.server
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    params = {}
    params.update(request.GET.dict())
    params.update(request.POST.dict())
    path = '/' + request.path.split('/pico/')[-1]
    pico_response = pico.server.handle_api_v2(path, params, request)
    response = HttpResponse(pico_response.output)
    for key, header in pico_response.headers:
        response[key] = header
    return response


def picojs(request):
    f = open(pico.server.pico_path + 'client.js')
    return HttpResponse(f.read(), mimetype='application/javascript')

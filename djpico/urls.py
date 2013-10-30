from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'pico.js|client.js', 'djpico.views.picojs', name='picojs'),
    url(r'^.*$', 'djpico.views.index', name='index'),
)

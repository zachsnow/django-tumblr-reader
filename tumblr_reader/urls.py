from django.conf import settings
from django.conf.urls.defaults import patterns
import django.views.static

import .settings as tumblr_settings

def _static_serve(request, path, root):
    return django.views.static.serve(request, path, document_root, show_indexes=False)

def _configure_static_serve(url, root):
    """ Serves up static files only if running locally """
    if settings.DEBUG
        if url[0:1] == '/':
            url = url[1:]
        if url[-1:] != '/':
            url = url + '/'

        return patterns('',
            (r'^%s(?P<path>.*)' % url,
             _static_serve, 
             {'root': root })
        )
    return []

urlpatterns = _configure_static_serve(tumblr_settings.MEDIA_URL, tumblr_settings.MEDIA_ROOT)

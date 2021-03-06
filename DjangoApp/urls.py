"""
Definition of urls for DjangoApp.
"""

from datetime import datetime
from django.conf.urls import url
from app.forms import BootstrapAuthenticationForm
from app.views import *
from app.models import *
from django.contrib.auth.views import *


# Uncomment the next lines to enable the admin:
from django.conf import settings

from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
     
    url(r'^$', home, name='home'),
    url(r'^contact$', contact, name='contact'),
    # url(r'^about', about, name='about'),
    # url(r'^login/$', login, {
    #          'template_name': 'app/login.html',
    #          'authentication_form': BootstrapAuthenticationForm,
    #          'extra_context':
    #          {
    #              'title':'Log in',
    #             'year':datetime.now().year,
    #          }
    #      },
    #      name='login'),
    # url(r'^logout$', logout, {  'next_page': '/'  },        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


    # from django.conf import settings
    #
    # # ... your normal urlpatterns here
    #
    # if settings.DEBUG:
    #     # static files (images, css, javascript, etc.)
    #     urlpatterns += ('',
    #                             (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #                                 'document_root': settings.MEDIA_ROOT}))
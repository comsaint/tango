from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'
    
    
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls', namespace="rango")), #look at module rango's urls.py
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls',namespace="registration")),
    # 'registration.backend.simple.urls' (1-step process) provides
    #registration -> /accounts/register/
    #registration complete -> /accounts/register/complete
    #login -> /accounts/login/
    #logout -> /accounts/logout/
    #password change -> /password/change/
    #password reset -> /password/reset/
    # for 2-step process, check out 'registration.backends.default.urls'
    # NOTE: 'django-registration-redux' does NOT provide the templates!
    # check 'https://github.com/macdhuibh/django-registration-templates' for some samples
)

# static media file deployment
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
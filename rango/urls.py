from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'), # http://<domain>.com/rango/, look at views.py's 'index'
        url(r'^about/', views.about, name='about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        # The Regex "(?P<category_name_slug>[\w\-]+)" matches any sequences
        # [\w\-]+  <==  one or more character(s) and hyphen
        # of alphanumeric characters (e.g. a-z, A-Z, or 0-9) and the hyphen(-)
        # before the trailing URL slash "/"
        )
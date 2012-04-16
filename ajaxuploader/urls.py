from django.conf.urls.defaults import patterns, url
from .views import AjaxFileUploader

urlpatterns = patterns(
    '',
#    url(r'start$', views.start, name="start"),
    url(r'ajax-upload$', AjaxFileUploader(), name="ajaxuploader"),
    )

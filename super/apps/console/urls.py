from django.conf.urls import url

from apps.console.views import SpiderConfigView, ProgressView, VisualizationView

urlpatterns = [
    url(r'^config/$', SpiderConfigView.as_view(), name='config'),
    url(r'^progress/$', ProgressView.as_view(), name='progress'),
    url(r'^visualization/$', VisualizationView.as_view(), name='visualization'),
]
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^console/', include('console.urls', namespace='console')),
]

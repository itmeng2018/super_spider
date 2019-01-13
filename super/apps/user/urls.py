from django.conf.urls import url

from apps.user.views import LoginView, RegisterView, VerRefreshView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^ver/$', VerRefreshView.as_view(), name='ver_code'),
]
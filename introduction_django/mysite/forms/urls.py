from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^$', views.base),
    url('^add-user/$', views.add_user),
]
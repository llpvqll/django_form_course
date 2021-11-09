from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.orm_base),
    url('^delete_user$', views.delete_user),
]



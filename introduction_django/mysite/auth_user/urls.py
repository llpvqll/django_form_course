from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.IndexForm.as_views()),
]

from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index),
    url(r'^batman$', views.batman),
    url(r'^joker$', views.joker),
    url(r'^batman_car', views.batman_car),
]




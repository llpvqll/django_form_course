from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.hello_django, name='hello_django'),
]




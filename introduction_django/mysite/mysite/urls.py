"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('^auth_user/', include('auth_user.urls')),
    url('^orm-less/', include('orm_less.urls')),
    url('^forms/', include('forms.urls')),
    url('^fourth_app/', include('fourth_app.urls')),
    url('^third_app/', include('third_app.urls')),
    url('^second_app/', include('second_app.urls')),
    url('admin/', admin.site.urls),
]



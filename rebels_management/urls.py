"""rebels_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth import login, logout
admin.autodiscover()

import blog
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', include('blog.urls')),
    path('', include('forum.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/login/$', login, name='login'),
    # re_path(r'^accounts/login/$', auth_views.LoginView.as_view()),
    re_path(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    # re_path( r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),
]

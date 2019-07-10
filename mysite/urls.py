"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('薬/', admin.site.urls), # 使用{% url 'admin:index' %}反向解析
    path('ckeditor', include('ckeditor_uploader.urls')), # 富文本文件地址
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('comment/', include(('comment.urls', 'comment'), namespace='comment')),
    path('api-auth/', include('rest_framework.urls')),
    path('',include(('blog.urls','blog'),namespace='blog')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
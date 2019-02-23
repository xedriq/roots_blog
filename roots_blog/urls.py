"""roots_blog URL Configuration

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
from django.urls import path, include

from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name='index'),
    path('blog/about/', blog_views.about, name='about'),
    path('blog/', include(('blog.urls','blog'), namespace='blog')),
    path('blog/add_blog/', include(('blog.urls','add_blog'), namespace='add_blog')),
    path('blog_detail/<int:id>', include(('blog.urls','blog_detail'), namespace='blog_detail')),
    path('blog/<int:id>/add_comment/', include(('blog.urls','add_comment'), namespace='add_comment')),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_blog/', views.add_blog, name = 'add_blog'),
    path('<int:id>/', views.blog_detail, name = 'blog_detail'),
    path('<int:id>/add_comment/', views.add_comment, name = 'add_comment'),
]

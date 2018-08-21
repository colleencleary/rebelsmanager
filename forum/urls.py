from django.urls import path, re_path
from . import views

urlpatterns = [
    path('forum', views.forum_list, name='forum_list'),
    path('forum/<int:pk>/', views.forum_detail, name='forum_detail'),
    path('forum/new', views.forum_new, name='forum_new'),
    path('forum/<int:pk>/edit/', views.forum_edit, name='forum_edit'),
    re_path(r'^forum/(?P<pk>\d+)/remove/$', views.forum_remove, name='forum_remove'),
    re_path(r'^forum/(?P<pk>\d+)/comment/$', views.add_comment_to_forumpost, name='add_comment_to_forumpost'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),


]

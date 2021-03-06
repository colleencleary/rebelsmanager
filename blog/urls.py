from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^post/comment/(?P<pk>\d+)/edit$', views.comment_edit, name='comment_edit'),
    re_path(r'^post/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    path('results/', views.BlogSearchListView.get_queryset, name='search_list_view'),

]

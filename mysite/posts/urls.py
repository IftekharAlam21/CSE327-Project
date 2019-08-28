from django.conf.urls import url,include
from django.contrib import admin
from posts import views


urlpatterns=[
             url(r'^$',views.PostListView.as_view(),name='post_list'),
             url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
             url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
             url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
             url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
            ]

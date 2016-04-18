from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required




urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^about/', TemplateView.as_view(template_name="about.html"),name='about'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/new/$', login_required(views.PostCreate.as_view(),login_url='login'), name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.PostEdit.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),

]

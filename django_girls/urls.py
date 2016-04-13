from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_girls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name': 'base.html'}),
    url('^',include('django.contrib.auth.urls')),
]

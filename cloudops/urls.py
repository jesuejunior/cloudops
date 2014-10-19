from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import ServerList, ServerNew, ApplicationNew, ApplicationList, ApplicationEdit, ApplicationDelete, ApplicationDetail, ServerDetail, ServerEdit, ServerDelete


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin', include(admin.site.urls)),
    url(r'^auth', 'rest_framework.authtoken.views.obtain_auth_token', name='auth'),
    url(r'^docs', include('rest_framework_swagger.urls')),
)


urlpatterns += patterns('api.views.server',
                        url(r'^servers$', ServerList.as_view(), name='server-list'),
                        url(r'^servers/new$', ServerNew.as_view(), name='server-new'),
                        url(r'^servers/(?P<pk>[\d]+)/detail$', ServerDetail.as_view(), name='server-detail'),
                        url(r'^servers/(?P<pk>[\d]+)/edit$', ServerEdit.as_view(), name='server-edit'),
                        url(r'^servers/(?P<pk>[\d]+)/delete$', ServerDelete.as_view(), name='server-delete'),
)

urlpatterns += patterns('api.views.application',
                        url(r'^applications$', ApplicationList.as_view(), name='application-list'),
                        url(r'^applications/new$', ApplicationNew.as_view(), name='application-new'),
                        url(r'^applications/(?P<pk>[\d]+)/detail$', ApplicationDetail.as_view(), name='application-detail'),
                        url(r'^applications/(?P<pk>[\d]+)/edit$', ApplicationEdit.as_view(), name='application-edit'),
                        url(r'^applications/(?P<pk>[\d]+)/delete$', ApplicationDelete.as_view(), name='application-delete'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
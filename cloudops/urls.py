from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.views import ServerList, ServerNew, ApplicationNew, ApplicationList, ApplicationEdit, ApplicationDelete, ApplicationDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^authentication/', 'rest_framework.authtoken.views.obtain_auth_token', name='auth'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)


urlpatterns += patterns('api.views.server',
                        url(r'^servers/$', ServerList.as_view(), name='server-list'),
                        url(r'^servers/new/$', ServerNew.as_view(), name='server-new'),

)

urlpatterns += patterns('api.views.application',
                        url(r'^applications/$', ApplicationList.as_view(), name='application-list'),
                        url(r'^applications/new/$', ApplicationNew.as_view(), name='application-new'),
                        url(r'^applications/(?P<pk>[\d]+)/detail$', ApplicationDetail.as_view(), name='application-detail'),
                        url(r'^applications/(?P<pk>[\d]+)/edit$', ApplicationEdit.as_view(), name='application-edit'),
                        url(r'^applications/(?P<pk>[\d]+)/delete$', ApplicationDelete.as_view(), name='application-delete'),

)

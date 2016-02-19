import sys

from django.conf.urls import patterns, url, include
from django.contrib import admin

from softdelete.views import ChangeSetList, ChangeSetUpdate, ChangeSetDetail

urlpatterns = patterns('softdelete.views',
                       url(r'^changeset/(?P<changeset_pk>\d+?)/undelete/$',
                           ChangeSetUpdate.as_view(),
                           name="softdelete.changeset.undelete"), 
                       url(r'^changeset/(?P<changeset_pk>\d+?)/$',
                           ChangeSetDetail.as_view(),
                           name="softdelete.changeset.view"),
                       url(r'^changeset/$',
                           ChangeSetList.as_view(),
                           name="softdelete.changeset.list"),
                       )

if 'test' in sys.argv:
    admin.autodiscover()
    urlpatterns += patterns('', url(r'^admin/', include(admin.site.urls)))
    urlpatterns += patterns('', url(r'^accounts/', include('registration.urls')))

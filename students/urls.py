# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'base.views.groups', name='groups'),
    url(r'^group/add/$', 'base.views.group_add', name='group_add'),
    url(r'^group/del/(?P<id>\d+)/$', 'base.views.group_del', name='group_del'),
    url(r'^group/info/(?P<id>\d+)/$', 'base.views.group_info', name='group_info'),
    url(r'^group/edit/(?P<id>\d+)/$', 'base.views.group_edit', name='group_edit'),

    url(r'^student/add/$', 'base.views.student_add', name='student_add'),
    url(r'^student/del/(?P<id>\d+)/$', 'base.views.student_del', name='student_del'),
    url(r'^student/edit/(?P<id>\d+)/$', 'base.views.student_edit', name='student_edit'),
    url(r'^login/$', 'base.views.user_login', name='user_login'),
    # url(r'^^students/', include('students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

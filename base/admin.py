# coding: utf-8

from django.contrib import admin
from base.models import Student, Group



class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'fio', 'bidthday', 'group',)
    list_filter = ('group',)
    ordering = ['group', 'fio']
    list_editable = ('fio', 'bidthday', 'group')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'elder',)
    list_editable = ('name', 'elder' )

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)



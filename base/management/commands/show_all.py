# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from base.models import Group, Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        groups = Group.objects.all()
        students = Student.objects.all()

        print 'Groups:'
        for group in groups:
            print '%s) %s %s' % (group.id, group.name, group.elder)

        print '\n Students:'
        for student in students:
            print "%s) %s %s %s" % (student.id, student.fio, student.bidthday, student.group)
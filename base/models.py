# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Student(models.Model):
    """
    Студент
    """
    fio = models.CharField(verbose_name=u'ФИО студента', blank=True, null=True, max_length=100)
    bidthday = models.DateField(verbose_name=u"Дата рождения", blank=True, null=True)
    group = models.ForeignKey('Group', verbose_name="Группа", blank=True, null=True, related_name="group")

    def __unicode__(self):
        return u"%s" % self.fio if self.fio else u"Студент №%s" % self.pk

    class Meta:
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенты"


class Group(models.Model):
    """
    Группа
    """
    name = models.CharField(verbose_name=u'Название группы', max_length=100, blank=True, null=True)
    elder = models.ForeignKey(Student, verbose_name=u"Староста", blank=True, null=True, related_name="elder")

    def __unicode__(self):
        return u"%s" % self.name if self.name else u"Група №%s" % self.pk

    class Meta:
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"



# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
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


class History(models.Model):
    """
    История создания / редактирования итд моделей
    """
    ACTION_TYPE = (
        (0, "Создание"),
        (1, "Редактирование"),
        (2, "Удаление"),
    )

    action = models.IntegerField(choices=ACTION_TYPE, verbose_name=u'Действие', default=1)
    date_action = models.DateTimeField(verbose_name=u'Время события', auto_now_add=True)
    model = models.CharField(verbose_name=u'Название модели', max_length=100)
    obj_id = models.IntegerField(verbose_name=u'Ид объекта')




from django.db.models import signals
from django.dispatch import receiver


def signal_obrab(sender, **kwargs):
    history = History()
    if "instance" in kwargs:
        obj = kwargs["instance"]
        action = 1
        if 'created' in kwargs and kwargs['created']:
            action = 0
        if not 'created' in kwargs:
            action = 2
        history.action = action
        history.model = sender.__name__
        history.obj_id = obj.pk
        history.save()



signals.post_save.connect(signal_obrab, sender=Student)
signals.post_save.connect(signal_obrab, sender=Group)
signals.post_delete.connect(signal_obrab, sender=Group)
signals.post_delete.connect(signal_obrab, sender=Student)
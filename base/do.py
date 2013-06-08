# -*- coding: utf-8 -*-
import os
import sys

path = os.path.normpath(os.path.join(os.getcwd(), '..'))
sys.path.append(path)

from django.core.management import setup_environ
import students.settings
setup_environ(students.settings)
from django.core.urlresolvers import reverse

from base.models import Student, Group
# Student.objects.create(fio="Карасев Александр", bidthday="1985-10-09")
# Group.objects.create(name="МТ-183", elder_id=1)

from django.test.client import Client
c = Client()
response = c.get('/', follow=True)
print response.status_code
print response.redirect_chain
url = response.redirect_chain[0][0]
print response.context
print url
response = c.post(url, data={'username': 'arhangel66', 'password': '09081985'}, follow=True)
print response.redirect_chain
print response.context
response = c.get('/')
print response.status_code
print response.context

#Зашли в создание групп
# url = reverse('group_info', 1)
url = '/group/info/1/'
print url
response = c.get(url)
# print response

#Создали группу
response = c.post(url, {'name': 'testgroup'})
print response.status_code
print dir(response)


#Зашли в создание студентов
# response = c.get(reversed('student_add'))
# print response.status_code

#Создали студента


#редактирование группы, назначили студента старостой


#Проверили, что есть теперь такая группа и такой студент

#Удалили группу

#Удалили студента




Student.objects.all().update(group=1)

def serialize():
    """
    Записать всё в файл
    """
    from django.core import serializers

    XMLSerializer = serializers.get_serializer("xml")
    xml_serializer = XMLSerializer()
    all_objects = list(Student.objects.all()) + list(Group.objects.all())
    with open("D:/test2.xml", "w") as out:
        xml_serializer.serialize(all_objects, stream=out)



def deserialize():
    """
    Записать из файла
    """
    from django.core import serializers
    data = open("D:/test2.xml")
    serializers.deserialize("xml", data, ignorenonexistent=True)
    for deserialized_object in serializers.deserialize("xml", data):
        if Student(deserialized_object):
            deserialized_object.save()
        if Group(deserialized_object):
            deserialized_object.save()


# print data
# print data2
deserialize()
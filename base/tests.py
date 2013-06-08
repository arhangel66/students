# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_login(self):
        """
        Авторизация
        """
        self.assertEqual(self.client.login(username='arh66', password='123456'), True)  # try to login

    def test_group_add(self):
        """
        Добавляю группу
        """
        url = reverse('group_add')
        self.assertEqual(self.client.post(url).status_code, 200)

        response = self.client.post(url, data={'name': 'testgroup'})
        self.assertEqual(response.context['result'], 'success')

    def test_student_add(self):
        """
        Добавляю студента
        """
        url = reverse('student_add')
        self.assertEqual(self.client.post(url).status_code, 200)

        response = self.client.post(url, data={'fio': 'My test student', 'bidthday': '1985-01-01'})
        self.assertEqual(response.context['result'], 'success')

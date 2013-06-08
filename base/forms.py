# -*- coding: utf-8 -*-
from django import forms
from base.models import Student, Group

class StudentForm(forms.ModelForm):
    """
    Форма студента
    """

    class Meta:
        model = Student


class GroupForm(forms.ModelForm):
    """
    Форма группы
    """

    class Meta:
        model = Group
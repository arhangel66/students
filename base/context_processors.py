# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings


def my_settings(request):
    """
    Возввращает настройки

    """
    return {'my_settings': settings}
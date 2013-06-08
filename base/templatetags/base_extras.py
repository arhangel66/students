# coding: utf-8
from django import template
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse


register = template.Library()
def get_admin_url(self):
    content_type = ContentType \
        .objects \
        .get_for_model(self.__class__)
    return reverse("admin:%s_%s_change" % (
        content_type.app_label,
        content_type.model),
        args=(self.id,))

@register.inclusion_tag('templatetags/edit_list.html', takes_context=False)
def edit_list(obj):
    """
    Возвращает ссылку на редактирование в админке
    """


    return {
        'url': get_admin_url(obj)

    }
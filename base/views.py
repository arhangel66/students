# -*- coding: utf-8 -*-

from base.models import Group, Student
from django.shortcuts import render_to_response, RequestContext, get_object_or_404, HttpResponseRedirect
from base.forms import GroupForm, StudentForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


#@login_required
def groups(request):
    groups = Group.objects.all()
    logout(request)
    return render_to_response('base/groups.html', locals(), context_instance=RequestContext(request))


#@login_required
def group_edit(request, id):
    """
    Редактирование группы
    """
    result = ''
    group = get_object_or_404(Group, pk=id)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            if form.save():
                result = 'success'

    else:
        form = GroupForm(instance=group)
        title = 'Редактирование группы'

    return render_to_response('base/form.html', locals(), context_instance=RequestContext(request))


#@login_required
def group_add(request):
    """
    Добавление группы
    """
    result = ''
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            if form.save():
                result = 'success'

    else:
        form = GroupForm()
        title = 'Добавление группы'

    return render_to_response('base/form.html', locals(), context_instance=RequestContext(request))


#@login_required
def group_del(request, id):
    """
    Удаление группы
    """
    result = ''
    if id:
        Group.objects.filter(pk=id).delete()
        result = 'success'
    return HttpResponseRedirect('/')


#@login_required
def group_info(request, id):
    """
    Информация о группе
    """
    group = get_object_or_404(Group, pk=id)
    students = Student.objects.filter(group_id = id)

    return render_to_response("base/group_info.html", locals(), context_instance=RequestContext(request))


#@login_required
def student_edit(request, id):
    """
    Редактирование студента
    """
    result = ''
    student = get_object_or_404(Student, pk=id)
    title = 'Редактирвоание студента %s' % student
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            if form.save():
                result = 'success'

    else:
        form = StudentForm(instance=student)


    return render_to_response('base/form.html', locals(), context_instance=RequestContext(request))


#@login_required
def student_add(request):
    """
    ДОбавление студента
    """
    result = ''
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            if form.save():
                result = 'success'

    else:
        form = StudentForm()
        title = 'Добавление студента'

    return render_to_response('base/form.html', locals(), context_instance=RequestContext(request))


#@login_required
def student_del(request, id):
    """
    Удаление студента
    """
    result = ''
    if id:
        Student.objects.filter(pk=id).delete()
        result = 'success'
    return HttpResponseRedirect('/')


def user_login(request):
    # вход в систему

    title = "вход в систему"
    if request.method == "POST":
        username = request.POST.get('username')
        if '@' in username:
            user = User.objects.filter(email=username)
            if user:
                username = user[0].username

        user = authenticate(username=u"%s" % username,
                            password=u"%s" % request.POST.get('password'))
        if user is not None:
            login(request, user)

            if 'next' in request.GET and request.GET['next']:
                return HttpResponseRedirect(request.GET['next'])

            else:
                return HttpResponseRedirect('/')

    return render_to_response('base/login.html', locals(), context_instance=RequestContext(request))


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

#Views for Students

def students_list(request):
	students = (
	{'id': 1,
	'first_name': u'Віталій',
	'last_name': u'Подоба',
	'ticket': 235,
	'image': 'img/flint.jpg'},
	{'id': 2,
	'first_name': u'Андрій',
	'last_name': u'Корост',
	'ticket': 2123,
	'image': 'img/charlz.jpg'},
	{'id': 3,
	'first_name': u'Елеонор',
	'last_name': u'Гатрі',
	'ticket': 264,
	'image': 'img/eleonor.jpg'},
	)
	header_groups = (
	{'group': u'МтМ - 21',
	'leader': u'Подоба Віталій',
	'leader_ticket': 235},
	{'group': u'МтМ - 22',
	'leader': u'Корост Андрій',
	'leader_ticket': 2123},
	)
	return render(request, 'students/students_list.html', {'students': students, 'GROUPS': header_groups})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

#Views for Groups

def groups_list(request):
	groups = (
	{'id': 1,
	'group_name': u'Мтм-21',
	'group_leader': u'Ячменєв Олег'},
	{'id': 2,
	'group_name': u'Мтм-22',
	'group_leader': u'Віталій Подоба'},
	{'id': 3,
	'group_name': u'Мтм-23',
	'group_leader': u'Іванов Андрій'},
	)
	header_groups = (
	{'group': u'МтМ - 21',
	'leader': u'Подоба Віталій',
	'leader_ticket': 235},
	{'group': u'МтМ - 22',
	'leader': u'Корост Андрій',
	'leader_ticket': 2123},
	)
	return render(request, 'students/groups_list.html', {'groups': groups, 'GROUPS': header_groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
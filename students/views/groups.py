# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Group

#Views for Groups

def groups_list(request):
	groups = Group.objects.all().order_by('id')
	
	header_groups = (
	{'group': u'МтМ - 21',
	'leader': u'Подоба Віталій',
	'leader_ticket': 235},
	{'group': u'МтМ - 22',
	'leader': u'Корост Андрій',
	'leader_ticket': 2123},
	)

	# try to order groups list
	order_by = request.GET.get('order_by', '')
	if order_by in ('title', 'leader__first_name', 'id'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()
	elif request.GET.get('reverse', '') == '1':
		groups = groups.reverse()

	# Paginate groups
	paginator = Paginator(groups, 3)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		groups = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		groups = paginator.page(paginator.num_pages)

	return render(request, 'students/groups_list.html', {'groups': groups, 'GROUPS': header_groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
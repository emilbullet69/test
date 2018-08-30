# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

#Views for Journal

def journal(request):
	journal = (
	{'id': 1,
	'name': u'Подоба Віталій',},
	{'id': 2,
	'name': u'Корост Андрій',},
	{'id': 3,
	'name': u'Притула Тарас',},
	)
	header_groups = (
	{'group': u'МтМ - 21',
	'leader': u'Подоба Віталій',
	'leader_ticket': 235},
	{'group': u'МтМ - 22',
	'leader': u'Корост Андрій',
	'leader_ticket': 2123},
	)
	return render(request, 'students/journal.html', {'journal': journal, 'GROUPS': header_groups})
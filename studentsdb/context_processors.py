def students_proc(request):
	return {'PORTAL_URL': request.scheme + r'://' + request.META['SERVER_NAME'] + ':' + request.META['SERVER_PORT']}
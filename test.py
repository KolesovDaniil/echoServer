def application(env, s_r):
	s_r('200 OK', [('Content-Type', 'text/plain')])
	print(env['QUERY_STRING'] == '')
	print(env['QUERY_STRING'])
	return [env['QUERY_STRING'].replace('&','\n')]

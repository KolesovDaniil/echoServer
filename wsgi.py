def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    body = [i + '\n' for i in environ['QUERY_STRING'].split('&')]
    return body

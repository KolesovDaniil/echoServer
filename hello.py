def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    body = [i + '\n' for i in environ['QUERY_STRING'].split('&')]
    body = [i.encode('ascii') for i in body]
    return body

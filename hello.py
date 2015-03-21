import urlparse

def app(environ, start_response):
	data = 'Hello, World!\n'
	query = urlparse.parse_qs(environ['QUERY_STRING'])
	for key in query.keys():
		for i in range(len(query[key])):
			data = data + key + ' = ' + query[key][i] + '\n'	
	status = '200 OK'
	response_headers = [
    	('Content-type','text/plain'),
    	('Content-Length', str(len(data)))
    ]
	start_response(status, response_headers)
	return iter(data)

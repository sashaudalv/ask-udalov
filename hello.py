import urlparse

def app(environ, start_response):
	data = '<html><body><h1>Hello World!</h1>\n<h2>Params:</h2>\n<ul>'
	#check if request body is clear
	try:
		requestBodySize = int(environ.get('CONTENT_LENGTH', 0))
	except:
		requestBodySize = 0
	#parse queries
	postQuery = urlparse.parse_qs(environ['wsgi.input'].read(requestBodySize))
	getQuery = urlparse.parse_qs(environ['QUERY_STRING'])
	
	#get parameters
	for key in getQuery.keys():
		for i in getQuery[key]:
			data += "<li>" + key + ' = ' + i + '</li>\n'

	#post parameters
	for key in postQuery.keys():
		for i in postQuery[key]:
			data += "<li>" + key + ' = ' + i + '</li>\n'	
	status = '200 OK'
	response_headers = [
    	('Content-type','text/html'),
    	('Content-Length', str(len(data)))
    ]
	start_response(status, response_headers)
	return data + "</ul></body></html>"

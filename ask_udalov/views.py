from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hello(request):
	data = '''
    <html>
        <head>
            <title>Hello world!</title>
        </head>
        <body>
        	<h1>Hello world!</h1>
        '''
	if request.method == 'GET':
		query =  request.GET.dict()
	elif request.method == 'POST':
		query =  request.POST.dict()

	for key in query.keys():
				data += '<p>' +  key + ' = ' + query[key] + '</p>'

	data += '''</body>
	</html>'''
	return HttpResponse(data)
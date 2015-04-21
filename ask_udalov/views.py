from django.http import HttpResponse
from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
#from django.http import Http404

#@csrf_exempt
#def hello(request):
#	data = '''
#   <html>
#        <head>
#            <title>Hello world!</title>
#        </head>
#        <body>
#        	<h1>Hello world!</h1>
#        	<ul>
#        '''
#	if request.method == 'GET':
#		query =  request.GET
#	elif request.method == 'POST':
#		query =  request.POST.dict()
#
#	for key in query.keys():
#				data += '<li>' +  key + ' = ' + str(query.getlist(key)) + '</li>'
#
#	data += '''</ul>
#		</body>
#	</html>'''
#	return HttpResponse(data)


from django.shortcuts import render
from django.http import Http404

# Create your views here.

def index(request):
	#try:
	#	page = int(request.GET.get('page', ' '))
	#except ValueError:
	#	raise Http404

	#data = {
	#	'query' : request.Get.get('query'),
	#	'page' : page
	#}
	return render(request, 'index.html', {'foo' : 'bar', 'questions' : [{'title' : 'sdad'},]})

def question(request):
	return render(request, 'question.html')

def ask(request):
	return render(request, 'ask.html')

def login(request):
	return render(request, 'login.html')

def signup(request):
	return render(request, 'signup.html')

def register(request):
	return render(request, 'register.html')
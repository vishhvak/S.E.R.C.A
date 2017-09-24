from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def form(request):
	return render(request, 'form.html')

def graph(request):
	return render(request, 'graph.html')

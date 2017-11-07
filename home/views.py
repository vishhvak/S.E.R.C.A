from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def form(request):
	return render(request, 'form.html')

def graph(request):
	if request.method == 'POST':
		lights = request.POST['lights']
		if lights:
			print(lights)
		return render(request, 'graph.html', 
			{'lights': lights} )
	else:
		return render(request, 'graph.html')
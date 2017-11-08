from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def form(request):
	return render(request, 'form.html')

def graph(request):
	if request.method == 'POST':
		lights = request.POST['lights']
		fans = request.POST['fans']
		TV = request.POST['TV']
		fridge = request.POST['fridge']
		wash = request.POST['wash']
		AC = request.POST['AC']
		shower = request.POST['shower']
		rest = request.POST['rest']
		fresh = request.POST['fresh']
		washdish = request.POST['washdish']
		drink = request.POST['drink']
		lightstime = request.POST['lightstime']
		fantime = request.POST['fantime']
		tvtime = request.POST['tvtime']
		ACtime = request.POST['ACtime']
		WMtime = request.POST['WMtime']
		if lights:
			print(lights)
		return render(request, 'graph.html', 
			{'lights': lights} )
	else:
		return render(request, 'graph.html')
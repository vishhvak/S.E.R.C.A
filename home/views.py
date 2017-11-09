from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def form(request):
	return render(request, 'form.html')

def graph(request):
	if request.method == 'POST':
		lights = request.POST.get('lights', False);
		fans = request.POST.get('fans', False);
		TV = request.POST.get('TV', False);
		fridge = request.POST.get('fridge', False);
		wash = request.POST.get('wash', False);
		AC = request.POST.get('AC', False);
		shower = request.POST.get('shower', False);
		rest = request.POST.get('rest', False);
		fresh = request.POST.get('fresh', False);
		washdish = request.POST.get('washdish', False);
		drink = request.POST.get('drink', False);
		lightstime = request.POST.get('lightstime', False);
		fantime = request.POST.get('fantime', False);
		tvtime = request.POST.get('tvtime', False);
		ACtime = request.POST.get('ACTime', False);
		WMtime = request.POST.get('WMTime', False);
		name = request.POST.get('name', False);
		lights=lights*2;
		if lights:
			print(lights)
		return render(request, 'graph.html', 
			{'lights': lights,
			 'name': name,
			 'fans': fans,
			 'TV': TV,
			 'fridge': fridge,
			 'wash': wash,
			 'AC': AC,
			 'shower': shower,
			 'rest': rest,
			 'fresh': fresh,
			 'washdish': washdish,
			 'drink': drink,
			 'lightstime': lightstime,
			 'fantime': fantime,
			 'tvtime': tvtime,
			 'ACtime': ACtime,
			 'WMtime': WMtime,
			 } )
	else:
		return render(request, 'graph.html')
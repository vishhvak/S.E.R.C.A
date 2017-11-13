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
		shower = round(int(request.POST.get('shower', False))*0.024*365);
		rest = round(int(request.POST.get('rest', False))*0.024*365);
		fresh = round(int(request.POST.get('fresh', False))*0.024*365);
		washdish = round(int(request.POST.get('washdish', False))*0.024*365);
		drink = round(int(request.POST.get('drink', False))*0.024*365);
		lightstime = request.POST.get('lightstime', False);
		fantime = request.POST.get('fantime', False);
		tvtime = request.POST.get('tvtime', False);
		ACtime = request.POST.get('ACtime', False);
		Rtime = request.POST.get('Rtime', False);
		WMtime = request.POST.get('WMTime', False);

		le = round(int(lights)*int(lightstime)*0.024*365)
		fe = round(int(fans)*int(fantime)*0.035*365)
		ace = round(int(AC)*int(ACtime)*0.542*365)
		tve = round(int(TV)*int(tvtime)*0.234*365)
		re = round(int(fridge)*int(Rtime)*0.234*365)
		wme = int(wash)*int(WMtime)
		return render(request, 'graph.html', 
			{'lights': lights,
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
			 'le': le,
			 'fe': fe,
			 'ace': ace,
			 'tve': tve,
			 're': re,
			 'wme': wme,
			 } )
	else:
		return render(request, 'graph.html')
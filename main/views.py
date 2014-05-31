from django.shortcuts import render, HttpResponse
from ipware.ip import get_ip

def home(request):
	ip = get_ip(request)
	ctx = {
		'ip': ip,
	}
	return render(request, 'home.html', ctx)

def survey(request):
	return render(request, 'survey.html')
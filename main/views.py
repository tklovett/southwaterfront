from django.shortcuts import render, HttpResponse
from ipware.ip import get_ip

from models import GroceryStore

def home(request):
	ip = get_ip(request)
	ctx = {
		'ip': ip,
	}
	return render(request, 'home.html', ctx)

def survey(request):
	ctx = {
		'stores': GroceryStore.objects.all()
	}
	return render(request, 'survey.html', ctx)
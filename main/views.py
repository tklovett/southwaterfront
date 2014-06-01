from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from ipware.ip import get_ip

from models import GroceryStore, Vote
from forms import ResidentForm

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

def resident(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ResidentForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            new_resident = form.save()
            for store_id in [x for x in request.POST.get('stores', "").split(",") if x != ""]:
                vote = Vote()
                vote.resident = new_resident
                vote.store_id = store_id
                vote.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ResidentForm() # An unbound form

    return render(request, 'resident.html', {
        'form': form,
        'stores': request.GET.get('stores', ""),
    })

def thanks(request):
    return HttpResponse("Thanks!")
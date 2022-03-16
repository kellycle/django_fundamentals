from django.shortcuts import render, redirect
import random
from time import localtime, strftime

# Create your views here.
def index(request):
    if 'gold' in request.session:
        context = {
            'activities': request.session['activities'],
            'date': strftime("(%Y/%m/%d %H:%M %p)", localtime()),
            'lost': "lost" 
        }
        request.session.save()
        return render(request, "index.html", context)
    else:
        request.session['gold'] = 0
        request.session['activities'] = []
        return render(request, "index.html")

def process(request):
    if request.POST['location'] == "farm":
        rand_num = random.randint(10,20);
        request.session['gold'] = request.session['gold'] + rand_num
        request.session['activities'].append(f"Earned {rand_num} golds from the {request.POST['location']}!")
    if request.POST['location'] == "cave":
        rand_num = random.randint(5,10)
        request.session['gold'] = request.session['gold'] + rand_num
        request.session['activities'].append(f"Earned {rand_num} golds from the {request.POST['location']}!")
    if request.POST['location'] == "house":
        rand_num = random.randint(2,5)
        request.session['gold'] = request.session['gold'] + rand_num
        request.session['activities'].append(f"Earned {rand_num} golds from the {request.POST['location']}!")
    if request.POST['location'] == "casino":
        earn_take = random.randint(1,2)
        if earn_take == 1:
            rand_num = random.randint(0,50)
            request.session['gold'] = request.session['gold'] + rand_num
            request.session['activities'].append(f"Entered a casino and won {rand_num} golds!!! Yay!!")
        else:
            rand_num = random.randint(0,50)
            request.session['gold'] = request.session['gold'] - rand_num
            request.session['activities'].append(f"Entered a casino and lost {rand_num} golds... Ouch..")
    return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")
from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    visit = request.session.get('visit')
    if visit is None:
        request.session['number'] = random.randint(1, 100)
        return render(request, "index.html")
    else:
        guess = request.session.get('guess')
        if guess is not None:
            context = {
                'guess': int(request.session['guess']),
                'number': int(request.session['number']),
                'visit': request.session.get('visit')
            }
            print(context)
            print(request.session['number'])
            return render(request, "index.html", context)
        else:
            return render(request, "index.html")

def process(request):
    if request.POST['guess'] == "":
        return redirect("/")
    else:
        request.session['guess'] = request.POST['guess']
        print(request.session['guess'])
        request.session['visit'] = 1
        return redirect("/")

# def show(request):
#     guess = request.session.get('guess')
#     if guess is not None:
#         context = {
#             'guess': int(request.session['guess']),
#             'number': int(request.session['number'])
#         }
#         print(context)
#         return render(request, "index2.html", context)
#     else:
#         pass
    

def clear(request):
    request.session.clear()
    return redirect("/")


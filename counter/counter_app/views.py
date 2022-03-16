from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    counter = request.session.get('counter', 1)
    request.session['counter'] = counter + 1
    if 'counter' in request.session:
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")
    context = {
        'counter' : counter,
    }
    return render(request, "index.html", context)

def destroy(request):
    del request.session['counter']     # clears a specific key
    return redirect("/")

# def add(request):
#     return redirect("/")
#     # counter = request.session.get('counter', 3)
#     # request.session['counter'] = counter + 2
#     # if 'counter' in request.session:
#     #     print('key exists!')
#     # else:
#     #     print("key 'key_name' does NOT exist")
#     # context = {
#     #     'counter' : counter,
#     # }
#     # return render(request, "index.html", context)
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # this is the route that shows the form
    return render(request, "index.html")

def create_user(request):
    # this is the route that process the form
    # print("Got Post Info.........")
    # print(request.POST)
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    # print(name_from_form)
    # print(email_from_form)
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }
    # return render(request, "show.html", context)
    return render(request, "success.html")

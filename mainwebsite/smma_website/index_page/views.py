from django.shortcuts import render , HttpResponse
from index_page.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    #return HttpResponse("home page")
    return render(request,"index/index.html")

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        reason = request.POST.get("reason")
        contact = Contact(name=name,email=email,reason=reason)
        contact.save()

        

    return render(request,"contact.html")

def hall_of_fame(request):
    return HttpResponse("this page will include the past businesses we have serviced")

def Services(request):
    return render(request,"Services.html")

def AboutUs(request):
    return render(request,"index/aboutus.html")
def signin(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        user = User.objects.create_user(username=username,email=Email,password=Password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return render(request,"index.html")
    return render(request, "signin.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            return render(request,"index.html")
        elif user is None:
            return HttpResponse("User does not exist")
    return render(request,"login.html")
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from trafficapp.forms import UserForm, TrafficRequestForm
from .models import TrafficGenerateRequest

from subprocess import check_output, run, PIPE
import sys 
import os

# Create your views here.
def index(request):
    return render(request, 'trafficapp/index.html')

# Register & Log In Views

@login_required
def special(request):
    return HttpResponse("You did it")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'trafficapp/registration.html', {'user_form': user_form, 'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active and user.is_superuser:
                login(request,user)
                return redirect('/trafficapp/admin/dashboard/', pk=user.username)
            else:
                login(request,user)
                return redirect('/trafficapp/user/dashboard/', pk=user.username) 
        else:
            print("Login Failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Details")
    else:
        return render(request, 'trafficapp/login.html',{})

# Admin Views

@login_required
def admindashboard(request):
    return render(request, 'trafficapp/admin/dashboard.html')

@login_required
def ordersplaced(request):
    obj = TrafficGenerateRequest.objects.all()
    context = {
        'objects': obj
    }
    return render(request, 'trafficapp/admin/orders.html', context)
    #return render(request, 'trafficapp/admin/orders.html')

@login_required
def adminpackages(request):
    return render(request, 'trafficapp/admin/packages.html')

@login_required
def userlist(request):
    return render(request, 'trafficapp/admin/users.html')

# User Views

@login_required
def userdashboard(request):
    return render(request, 'trafficapp/user/dashboard.html')

@login_required
def placeorder(request):
    return render(request, 'trafficapp/user/placeorder.html')

@login_required
def userpackages(request):
    return render(request, 'trafficapp/user/packages.html')

@login_required
def history(request):
    return render(request, 'trafficapp/user/history.html')

# Traffic Process URLs

@login_required
def traffic_request(request):
    if request.method == "POST":
        traffic_request_form = TrafficRequestForm(data=request.POST)

        if traffic_request_form.is_valid():
            traffic_request = traffic_request_form.save(commit=False)
            traffic_request.user = request.user
            traffic_request.save()
        else:
            print(traffic_request_form.errors)
    else:
        traffic_request_form = TrafficRequestForm()
    
    return redirect('/trafficapp/user/dashboard/')

@login_required
def generate_traffic(request):
    pk_id = request.GET['id']
    user = request.GET['user']
    url = request.GET['url']
    minimum = request.GET['minimum']
    maximum = request.GET['maximum']
    requests = request.GET['requests']
    stay = request.GET['stay']

    #output = check_output([python traffic.py, "--domain" , url])
    #print(sys.argv)
    out = run([sys.executable, 'C://Users//Maisum Abbas//learning_users//trafficapp//traffic.py', "--domain", url, "--threads", '5', "--max-clicks", maximum, "--min-clicks", minimum, "--stay", stay, "--requests", requests])
    #os.system(out)
    return redirect('/trafficapp/admin/dashboard/')
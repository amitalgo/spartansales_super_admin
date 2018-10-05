from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from django.urls import reverse
# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if(user):
            login(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            context['error']="Please provide valid credentials."
            return render(request,'authh/index.html', context)
    else:
        return render(request,"authh/index.html", context)




def logout_user(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('home'))

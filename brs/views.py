from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import bookingsForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def logins(request):
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    user = authenticate(request, username=username, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"registration/login.html")

@login_required
def booking(request):
    if request.method == "POST":
        form = bookingsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=bookingsForm()
        dict_form={
            'form':form,
    }
        return render(request,'booking.html',dict_form)


def logouts(request):
    logout(request)
    return redirect('login')

def signup(request):
        if request.method == "POST":
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exits')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('home')
        else:
            return render(request,'signup.html')

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = UserCreationForm()

    return render(request,'register.html',{'form':form})

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            print(username)
            password = request.POST["password"]
            print(password)
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("dashboard")
            else:
                return redirect("log_in")

        return render(request,'login.html')
    else:
        return redirect("dashboard")

@login_required(login_url = "log_in")
def dashboard(request):
    messages.success(request,"Successfully Logged In")
    return render(request,'dashboard.html',{"user": request.user})

def log_out(request):
    logout(request)
    return redirect("log_in")
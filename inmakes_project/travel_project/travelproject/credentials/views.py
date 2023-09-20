from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials ')
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method =='POST':
        first_Name = request.POST['first_Name']
        last_Name = request.POST['last_Name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['Password']
        cpassword = request.POST['Password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is taken")
                return redirect("register")
            else:
                 user=User.objects.create_user(first_name=first_Name,last_name=last_Name,email=email,username=username,password=password)

                 user.save()
                 print("user created")
                 return redirect("login")
        else:
            messages.info(request, "password is not matched")
            return redirect("register")
        return redirect("/")

    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
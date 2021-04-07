from django.shortcuts import render,redirect
from account.models import Account
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from owner.models import Owner
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request,'homepage.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            account = Account(email=email, password=make_password(p1), is_owner=True)
            account.save()
            messages.success(request,"Account created successfully")
            owner = Owner(name=name, contact=contact, address=address, account_id=account.id)
            owner.save()
            messages.success(request,"owner added successfully")
            return redirect('login')
        else:
            return redirect('register')

def loginowner(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('ownerpage')
        else:
            messages.error(request,"Wrong Email or Password!!! please input the right email and password")
            return redirect('login')

def signout(request):
    logout(request)
    return redirect('home')
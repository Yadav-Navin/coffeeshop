
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_process,logout as logout_process
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['cpassword']
        email = request.POST['email']

        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user alredy exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email alredy exists')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'password and conform password are not matched')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_process(request,user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    logout_process(request)
    return redirect('/')

def recoverPassword(request):
    if request.method == 'POST':
        username = request.POST['username']
        Newpassword = request.POST['password']

        if User.objects.filter(username=username).exists():
            update_password = User.objects.get(username=username)
            update_password.set_password(Newpassword)
            update_password.save()
            return redirect('login')
        else:
            messages.info(request,'Username does not exists please Register')
            return redirect('register')
        
    else:
        return render(request,'passwordChange.html')
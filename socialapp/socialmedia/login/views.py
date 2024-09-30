from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth import authenticate, login as auth_log
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomAuthenticationForm
from .forms import user_signup
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse("User does not exist")
        if user.check_password(password):    
            auth_log(request, user)
            messages.success(request, 'user successfully logged in')
            return redirect('/account/')
        else:
            messages.error(request, 'invalid username or password')
            return redirect('/login/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = user_signup(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username , password=password)
            user.save()
            auth_log(request , user)
            return redirect('home')
        else:
            form = user_signup()
            return render(request , 'sign_up.html' , {'form': form})
    else:
        form = user_signup()
        return render(request , 'sign_up.html' , {'form': form})
def user_logout(request):
    logout(request)
    redirect('signup')
    
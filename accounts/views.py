from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import loginForm, registerUser
from django.contrib import messages
from .models import Profile

@user_passes_test(lambda u: not u.is_authenticated , '/' , None)
def user_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully', 'success')
                return redirect('/')
            else:
                messages.error(request, 'The username or password is incorrect', 'danger')
    else:
        form = loginForm()
    return render(request, 'accounts/login.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('accounts:login')

@user_passes_test(lambda u: not u.is_authenticated , '/' , None)
def user_register(request):
    if request.method == 'POST':
        form = registerUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(first_name=cd['first_name'], last_name=cd['last_name'], email=cd['email'], username=cd['username'], password=cd['password'])
            p1 = Profile(user=user, phone=cd['phone'], age=cd['age'])
            p1.save()
            login(request, user)
            return redirect('/')
    else:
        form = registerUser()
    return render(request, 'accounts/register.html', {'form':form})
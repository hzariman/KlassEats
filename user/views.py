from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, get_user_model, login, logout

from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

""" def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form' : form,
    }
    return render(request, 'user/login.html', context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "user/register.html", context) """


def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email, password = raw_password)
            login(request,account)
            return redirect('/')
            
    else:
        form = UserRegisterForm()
    
    return render(request, 'user/register.html', {'form':form})

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/')

    if request.POST:
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email = email, password= password)

            if user:
                login(request, user)
                return redirect('/')
    else:
        form = UserLoginForm()

    return render(request,'user/login.html', {'form' : form})


    
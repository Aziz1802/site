from django.shortcuts import render
from apps.user.forms import UserRegistrationForm, UserLoginForm ,UserProfileform
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Вы успешно зарегались')
        return HttpResponseRedirect('/')
    else:
        form = UserRegistrationForm()
    return render (request, 'registration.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def profile(request):
    if request.method == 'POST':
        form = UserProfileform(data=request.POST,
        isinstance=request.user,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/profile')
    else:
        form=UserProfileform(isinstance=request)
        return render(request,'profile.html',{'form':form})




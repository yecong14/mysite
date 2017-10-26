from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.
def user_login(request):
    if request.method == 'POST':
         login_form = LoginForm(request.POST)
         if login_form.is_valid():
             cd = login_form.cleaned_data
             user = authenticate(username=cd['username'],password=cd['password'])
             if user:
                 return HttpResponse('Wellcom! You have been authenticated successfully!')
             else:
                 return HttpResponse('Sorry. Your username or you password is not right.')
         else:
             return HttpResponse('Invalid login')

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'account/login.html',{'form':form})

from django.shortcuts import render
from .forms import LoginForm,RegistrationForm,UserProfileForm
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

def register(request):
	if request.method == 'POST':
		user_form = RegistrationForm(request.POST)
		userprofile_form = UserProfileForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			new_profile = userprofile_form.save(commit=False)
			new_profile.user = new_user
			new_profile.save()
			return HttpResponse('registe successfully')
		else:
			return HttpResponse('sorry,you can not register')
	else:
		user_form = RegistrationForm()
		userprofile_form = UserProfileForm()
		return render(request,'account/register.html',{'form':user_form,'profile':userprofile_form})

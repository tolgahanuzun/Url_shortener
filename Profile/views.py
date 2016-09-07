# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core.exceptions import ValidationError
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from Profile.models import Profile
from Profile.forms import LoginForm, RegistrationForm

# Create your views  here.
def login(request):
	if not request.user.is_authenticated():
		context = {}
		try:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				auth_login(request, user)
				return HttpResponseRedirect("/")
			else:
				context['error'] = 'Non active user'
				
		except:
			context['error'] = ''
			
		populateContext(request, context)	
		return render(request, 'login.html', context)

	else:
		return HttpResponseRedirect("/index/")

def populateContext(request, context):
	context['authenticated'] = request.user.is_authenticated()

	if context['authenticated'] == True:
		context['username'] = request.user.username


def logout(request):
	auth_logout(request)
	return redirect('/')

def register(request): 
	if not request.user.is_authenticated():
		form = RegistrationForm()

		if request.method == "POST":
			form = RegistrationForm(request.POST)

			if  form.is_valid():
				form.save()       
				return render(request,"/index",
								   locals())
			else:
				form = RegistrationForm()
				return render(request,"register.html",
								   locals())
		else:
			form = RegistrationForm()
			return render(request, "register.html",{'form':form})

	else:
		return HttpResponseRedirect("/index/")    
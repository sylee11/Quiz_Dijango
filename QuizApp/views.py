from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm , ForgetPassForm ,QuizForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Question
# Create your views here.

def login(request):
	loginForm = LoginForm()
	if request.method == "POST" :
		a = request.POST['userName']
		b = request.POST['passWord']
		user = authenticate(request, username=a, password=b)
		if user is not None:
			# login(request, user)
			return render(request, 'home.html')
		else:
			return HttpResponse('Fail')
        # Return an 'invalid login' error message.
		# try:
		# 	User.objects.get(username = a, password = b)
		# 	#return HttpResponse(User.objects.get(username = a))
		# except User.DoesNotExist:
		# 	return HttpResponse('Fail')

	if  request.user.is_authenticated:
		return redirect('home')
	return render(request, 'login.html', {'form': loginForm })

def home(request):
	quiz = QuizForm()
	allq = Question.objects.all()
	b = allq[0].id
	return render(request, 'home.html', {'form': allq})

def logout_view(request):
	logout(request)
	loginForm = LoginForm()
	#return render(request, 'login.html',{'form': loginForm })
	return redirect('login')

def register(request):
	registerForm = RegisterForm()
	if request.method == 'POST':
		registerForm = RegisterForm(request.POST)
		if registerForm.is_valid():
			registerForm.save()
			return HttpResponseRedirect('/')
	return render(request, 'register.html', {'form': registerForm})

def forgetPass(request):
	formForget = ForgetPassForm()

	#if request.method == "POST":
	return render(request, 'forgetpass.html', {'form' : formForget})
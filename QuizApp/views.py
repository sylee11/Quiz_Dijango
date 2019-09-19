from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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
	return render(request, 'home.html')

def logout_view(request):
	logout(request)
	loginForm = LoginForm()
	#return render(request, 'login.html',{'form': loginForm })
	return redirect('login')
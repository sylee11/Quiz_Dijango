from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.login, name='login'),
	path('home', views.home, name='home'),
	path('logout', views.logout_view, name='logout')
]
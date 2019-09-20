from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	#path('', views.login, name='login'),
	path('home', views.home, name='home'),
	path('logout', views.logout_view, name='logout'),
	path('regisrer', views.register, name='register'),
	path('forget', views.forgetPass, name='forgetPass'),
	#path('login', auth_views.login, {'template_name':'logig.html'}, name='login2'),
	path( r'',auth_views.LoginView.as_view(template_name="login.html"), name="login2"),
	url( r'^logout/$', auth_views.LogoutView.as_view(next_page='home'), name='logout2')

]
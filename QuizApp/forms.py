from django import forms
from django.contrib.auth.models import User
from . models import Question
import re
from  django.core.exceptions import ObjectDoesNotExist
class LoginForm(forms.Form):
	userName = forms.CharField(label='User', max_length =100)
	passWord = forms.CharField(label="Password", max_length=100, widget =forms.PasswordInput())

class RegisterForm(forms.Form):
	userName = forms.CharField(label='User' ,max_length=100)
	email = forms.EmailField(label ='Email')
	passWord = forms.CharField(label='Password', max_length=100, widget = forms.PasswordInput())
	passWord2 = forms.CharField(label ='NHập lại Password', max_length=100, widget = forms.PasswordInput())

	def clean_passWord2(self):
		if 'passWord' in self.cleaned_data:
			passWord = self.cleaned_data['passWord']
			passWord2 = self.cleaned_data['passWord2']
			if passWord == passWord2 and passWord:
				return passWord2
		raise forms.ValidationError('Mat khẩu sai')
	def clean_userName(self):
		userName = self.cleaned_data['userName']
		if not re.search(r'^\w+$' ,userName):
			raise forms.ValidationError('Sai user')
		try:
			User.objects.get(username =userName)
		except ObjectDoesNotExist:
			return userName
		raise forms.ValidationError('User exist')
		
	def save(self):
		User.objects.create_user(username = self.cleaned_data['userName'], password = self.cleaned_data['passWord'],email = self.cleaned_data['email'])

class ForgetPassForm(forms.Form):
	email = forms.EmailField(label="Email")

	# def checkExistMail(self):
	# 	email = self.cleaned_data['email']
		
class QuizForm(forms.Form):
	u = Question.objects.get(id = "1")
	allq = Question.objects.all()
	print(type(allq))
	for x in allq:
		FAVORITE_COLORS_CHOICES = [
		('anser1', allq[0].anser1 ),
		('anser1', u.anser2),
		('anser1', u.anser3),
		('anser4', u.anser4),
		]
		# numberQuestion = forms.IntegerField(label="Câu hỏi")
		# question = forms.CharField()
		choseAnser = forms.MultipleChoiceField(
			required=False,
			widget = forms.CheckboxSelectMultiple,
			choices = FAVORITE_COLORS_CHOICES
		)
	#item = forms.ChoiceField(choices=BIRTH_YEAR_CHOICES)
	
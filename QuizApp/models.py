from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return(self.name)
		
class Question(models.Model):
	question = models.CharField(max_length =40, blank = True, null = True)
	anser1 = models.CharField(max_length= 50, null = True)
	anser2 = models.CharField(max_length= 50, null = True)
	anser3 = models.CharField(max_length= 50, null = True)
	anser4 = models.CharField(max_length= 50, null = True)
	anser = models.IntegerField()
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	category_id = models.ForeignKey(Category, on_delete = models.CASCADE)
	def __str__(self):
		return(self.question)

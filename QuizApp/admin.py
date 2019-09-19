from django.contrib import admin
from .models import Category, Question
# Register your models here.

#admin.site.register(Category)
#admin.site.register(Question)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
admin.site.register(Category, CategoryAdmin)

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['id', 'question' , 'anser', 'category_id']
	search_fields = ['question']
admin.site.register(Question, QuestionAdmin)

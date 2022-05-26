from django.contrib import admin

from .models import Blog, Comment

# Register your models here.

admin.site.register(Blog) # admin site에서 Blog 객체를 확인하기 위한 절차
admin.site.register(Comment)
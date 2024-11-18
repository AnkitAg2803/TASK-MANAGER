# admin.py in tasks app
from django.contrib import admin
from .models import Task

admin.site.register(Task)

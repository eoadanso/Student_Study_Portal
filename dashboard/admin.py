from django.contrib import admin
from django.contrib.admin.decorators import register

from dashboard.models import Notes
from . models import *

# Register your models here.

admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)
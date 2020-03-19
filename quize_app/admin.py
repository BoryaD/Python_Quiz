from django.contrib import admin
from .models import Quiz,  Option, Riddle
# Register your models here.

admin.site.register(Quiz)
admin.site.register(Option)
admin.site.register(Riddle)

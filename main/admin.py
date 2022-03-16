from django.contrib import admin
from .models import Chembti, Question, Choice

admin.site.register(Chembti)
admin.site.register(Question)
admin.site.register(Choice)
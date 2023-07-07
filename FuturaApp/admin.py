from django.contrib import admin

from FuturaApp import models

# Register your models here.
admin.site.register(models.Intern)
admin.site.register(models.Coding_question)
admin.site.register(models.Noncoding_question)
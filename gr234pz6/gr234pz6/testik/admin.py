from django.contrib import admin
from .models import *
# Register your models here.
class AnswersAdmin(admin.ModelAdmin):
    list_display = ['title', 'Users', 'Skills','Score', 'Date']
admin.site.register(Answers, AnswersAdmin)

class SertifAdmin(admin.ModelAdmin):
    list_display = ['title', 'Users', 'Blank','Date', 'Filled_sertif']
admin.site.register( Sertif, SertifAdmin)
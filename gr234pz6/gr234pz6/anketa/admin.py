from django.contrib import admin
from .models import *


# Register your models here.
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Professions, ProfessionAdmin)

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Skills, SkillsAdmin)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'Score', 'Skills']
admin.site.register(Questions, QuestionsAdmin)

class Model_profAdmin(admin.ModelAdmin):
    list_display = ['title', 'Professions', 'Skills','Score']
admin.site.register(Model_prof, Model_profAdmin)

class BlankAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_full', 'image_one']
admin.site.register( Blank, BlankAdmin)

class HumanAdmin(admin.ModelAdmin):
    list_display = ['title', 'avatar', 'phone']
admin.site.register( Human, HumanAdmin)


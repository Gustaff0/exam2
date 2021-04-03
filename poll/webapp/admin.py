from django.contrib import admin
from webapp.models import Poll, Choice, Answer

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_filter = ['created_at', 'question']
    search_fields = ['question']
    fields = ['id', 'question']
    readonly_fields = ['created_at','id']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text', 'poll']
    list_filter = ['poll']
    search_fields = ['choice_text']
    fields = ['id', 'choice_text', 'poll']
    readonly_fields = ['id']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice', 'poll', 'created_at']
    list_filter = ['poll']
    search_fields = ['poll', 'choice']
    fields = ['id', 'choice', 'poll']
    readonly_fields = ['id', 'created_at']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)

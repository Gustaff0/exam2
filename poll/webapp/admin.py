from django.contrib import admin
from webapp.models import Poll, Choice

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

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)

from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Info', {'fields': ['question_txt']}),
        ('Date Info', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_txt', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
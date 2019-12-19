from django.contrib import admin
from .models import Reflection
from .models import Question
from .models import QuestionSubmission
from .models import Submission


class QuestionAdmin(admin.TabularInline):
    model = Question
    fields = []
    extra = 0


class QuestionSubmissionAdmin(admin.TabularInline):
    model = QuestionSubmission
    fields = []
    readonly_fields = ("question__prompt", "answer")
    extra = 0


class ReflectionAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin]
    readonly_fields = ()
    list_filter = []


class SubmissionAdmin(admin.ModelAdmin):
    inlines = [QuestionSubmissionAdmin]
    readonly_fields = ("reflection", "user")

    list_filter = ["reflection"]


admin.site.register(Reflection, ReflectionAdmin)
admin.site.register(Submission, SubmissionAdmin)


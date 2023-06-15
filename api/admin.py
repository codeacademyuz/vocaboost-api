from django.contrib import admin

from .models import (
    Word, Topic,
    Student, StudentWord
)


admin.site.register(Topic)
admin.site.register(Word)
admin.site.register(Student)
admin.site.register(StudentWord)

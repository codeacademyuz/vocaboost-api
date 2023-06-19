from django.contrib import admin

from .models import (
    Word, Topic,
    Student, StudentWord,
    WordImage, TopicImage,
)


admin.site.register(Topic)
admin.site.register(Word)
admin.site.register(Student)
admin.site.register(StudentWord)
admin.site.register(WordImage)
admin.site.register(TopicImage)

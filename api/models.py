from django.db import models
from django.core.validators import MinValueValidator


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Word(models.Model):
    name  = models.CharField(max_length=128, unique=True)
    image = models.CharField(max_length=128, unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='words')
    attempts = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    corrects = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.topic.name}: {self.name}'


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    chat_id = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.first_name


class StudentWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='words')
    attempts = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    corrects = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.student.first_name}: {self.word.name}'

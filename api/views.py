from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

import random

from .models import (
    Word, Topic,
    Student, StudentWord
)

from .serializers import (
    WordSerializer, TopicSerializer,
    StudentSerializer, StudentWordSerializer
)


class TopicView(APIView):
    """
    List all topics.
    """
    def get(self, request: Request, pk: int = None):
        if pk:
            try:
                topic = Topic.objects.get(pk=pk)
                serializer = TopicSerializer(topic)
                return Response(serializer.data)
            except Topic.DoesNotExist:
                return Response({'status': 'Topic does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            topics = Topic.objects.all()
            serializer = TopicSerializer(topics, many=True)
            return Response(serializer.data)
    
    def post(self, request: Request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, pk: int):
        try:
            topic = Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            return Response({'status': 'Topic does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int):
        try:
            topic = Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            return Response({'status': 'Topic does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class WordView(APIView):
    """
    List all words.
    """
    def get(self, request: Request, pk: int = None):
        if pk:
            try:
                word = Word.objects.get(pk=pk)
                serializer = WordSerializer(word)
                return Response(serializer.data)
            except Word.DoesNotExist:
                return Response({'status': 'Word does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            words = Word.objects.all()
            serializer = WordSerializer(words, many=True)
            return Response(serializer.data)
    
    def post(self, request: Request):
        data = request.data
        topic_name = data.get('topic')
        try:
            topic = Topic.objects.get(name=topic_name)
        except Topic.DoesNotExist:
            topic = Topic.objects.create(name=topic_name)
        data['topic'] = topic.id
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, pk: int):
        try:
            word = Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            return Response({'status': 'Word does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int):
        try:
            word = Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            return Response({'status': 'Word does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class StudentView(APIView):
    """
    List all students.
    """
    def get(self, request: Request, pk: int = None):
        if pk:
            try:
                student = Student.objects.get(pk=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'status': 'Student does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
    
    def post(self, request: Request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, pk: int):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'status': 'Student does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'status': 'Student does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentWordView(APIView):
    """
    List all student words.
    """
    def get(self, request: Request, pk: int = None):
        if pk:
            try:
                student_word = StudentWord.objects.get(pk=pk)
                serializer = StudentWordSerializer(student_word)
                return Response(serializer.data)
            except StudentWord.DoesNotExist:
                return Response({'status': 'Student word does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            student_words = StudentWord.objects.all()
            serializer = StudentWordSerializer(student_words, many=True)
            return Response(serializer.data)
    
    def post(self, request: Request):
        serializer = StudentWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, pk: int):
        try:
            student_word = StudentWord.objects.get(pk=pk)
        except StudentWord.DoesNotExist:
            return Response({'status': 'Student word does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentWordSerializer(student_word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int):
        try:
            student_word = StudentWord.objects.get(pk=pk)
        except StudentWord.DoesNotExist:
            return Response({'status': 'Student word does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        student_word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetRandomWordView(APIView):
    """
    Get a random word.
    """
    def get(self, request: Request, chat_id: int):
        try:
            student = Student.objects.get(chat_id=chat_id)
        except Student.DoesNotExist:
            return Response({'status': 'Student does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Get random word
        words = Word.objects.all()
        random_word = random.choice(words)
        # create student word
        try:
            student_word = StudentWord.objects.get(student=student, word=random_word)
        except StudentWord.DoesNotExist:
            student_word = StudentWord.objects.create(student=student, word=random_word)
        # update word attempts
        random_word.attempts += 1
        student_word.attempts += 1
        # update word last attempt
        random_word.save()
        student_word.save()
        # serialize word
        serializer = WordSerializer(random_word)
        return Response(serializer.data)


class CheckAnswerView(APIView):
    """
    Check if answer is correct.
    """
    def get(self, request: Request, chat_id: int, word_id: int, answer: str):
        try:
            student = Student.objects.get(chat_id=chat_id)
        except Student.DoesNotExist:
            return Response({'status': 'Student does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            word = Word.objects.get(pk=word_id)
        except Word.DoesNotExist:
            return Response({'status': 'Word does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        # create student word
        try:
            student_word = StudentWord.objects.get(student=student, word=word)
        except StudentWord.DoesNotExist:
            student_word = StudentWord.objects.create(student=student, word=word)
        # update word attempts
        word.attempts += 1
        student_word.attempts += 1
        # check answer
        if answer.lower().strip() == word.name.lower():
            word.corrects += 1
            student_word.corrects += 1
            word.save()
            student_word.save()
            return Response({'is_correct': True, 'name': word.name})
        else:
            word.save()
            student_word.save()
            return Response({'is_correct': False, 'name': word.name})
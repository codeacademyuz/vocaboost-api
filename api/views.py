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
    def get(self, request: Request):
        words = Word.objects.all()
        random_word = random.choice(words)
        serializer = WordSerializer(random_word)
        return Response(serializer.data)

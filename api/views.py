from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

# radom module is used to get random words
import random

# import models and serializers
from .models import (
    Word, Topic,
    Student, StudentWord,
    WordImage, TopicImage,
)
from .serializers import (
    WordSerializer, TopicSerializer,
    StudentSerializer, StudentWordSerializer,
    WordImageSerializer, TopicImageSerializer,
)


class TopicList(APIView):
    """
    List all topics, or create a new topic.
    """
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):
        # get data
        data = request.data
        # get topic images
        topic_images = data.pop('topic_images')
        # create topic
        serializer = TopicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # create topic images
            for topic_image in topic_images:
                topic_image_data = {
                    'topic': serializer.data['id'],
                    'image': topic_image
                }
                topic_image_serializer = TopicImageSerializer(
                    data=topic_image_data
                )
                if topic_image_serializer.is_valid():
                    topic_image_serializer.save()
                else:
                    return Response(
                        topic_image_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                    )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TopicDetail(APIView):
    """
    Retrieve, update or delete a topic instance.
    """
    def get_object(self, pk):
        try:
            return Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            return False

    def get(self, request, pk):
        topic = self.get_object(pk)
        if topic:
            serializer = TopicSerializer(topic)
            return Response(serializer.data)
        return Response(
            {'error': 'Topic not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    def put(self, request, pk):
        topic = self.get_object(pk)
        if topic:
            serializer = TopicSerializer(topic, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'error': 'Topic not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk):
        topic = self.get_object(pk)
        if topic:
            topic.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'error': 'Topic not found'},
            status=status.HTTP_404_NOT_FOUND
        )


class WordList(APIView):
    """
    List all words, or create a new word.
    """
    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self, request):
        # create a new topic
        data = request.data
        # get topic
        data['topic'] = Topic.objects.get(pk=data['topic']).id
        # get word images
        word_images = data.pop('word_images')
        # create word
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # create word images
            for word_image in word_images:
                word_image_data = {
                    'word': serializer.data['id'],
                    'image': word_image
                }
                word_image_serializer = WordImageSerializer(
                    data=word_image_data
                )
                if word_image_serializer.is_valid():
                    word_image_serializer.save()
                else:
                    return Response(
                        word_image_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                    )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class WordDetail(APIView):
    """
    Retrieve, update or delete a word instance.
    """
    def get_object(self, pk):
        try:
            return Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            return False

    def get(self, request, pk):
        word = self.get_object(pk)
        if word:
            serializer = WordSerializer(word)
            return Response(serializer.data)
        return Response(
            {'error': 'Word not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    def put(self, request, pk):
        word = self.get_object(pk)
        if word:
            serializer = WordSerializer(word, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'error': 'Word not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk):
        word = self.get_object(pk)
        if word:
            word.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'error': 'Word not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    

class StudentList(APIView):
    """
    List all students, or create a new student.
    """
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class StudentDetail(APIView):
    """
    Retrieve, update or delete a student instance.
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return False

    def get(self, request, pk):
        student = self.get_object(pk)
        if student:
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        return Response(
            {'error': 'Student not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    def put(self, request, pk):
        student = self.get_object(pk)
        if student:
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'error': 'Student not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk):
        student = self.get_object(pk)
        if student:
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'error': 'Student not found'},
            status=status.HTTP_404_NOT_FOUND
        )


class StudentWordList(APIView):
    """
    List all student words, or create a new student word.
    """
    def get(self, request):
        student_words = StudentWord.objects.all()
        serializer = StudentWordSerializer(student_words, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class StudentWordDetail(APIView):
    """
    Retrieve, update or delete a student word instance.
    """
    def get_object(self, pk):
        try:
            return StudentWord.objects.get(pk=pk)
        except StudentWord.DoesNotExist:
            return False

    def get(self, request, pk):
        student_word = self.get_object(pk)
        if student_word:
            serializer = StudentWordSerializer(student_word)
            return Response(serializer.data)
        return Response(
            {'error': 'Student word not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    def put(self, request, pk):
        student_word = self.get_object(pk)
        if student_word:
            serializer = StudentWordSerializer(student_word, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'error': 'Student word not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk):
        student_word = self.get_object(pk)
        if student_word:
            student_word.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'error': 'Student word not found'},
            status=status.HTTP_404_NOT_FOUND
        )


class StudentWordListByStudent(APIView):
    """
    List all student words by student id.
    """
    def get(self, request, pk):
        student_words = StudentWord.objects.filter(student=pk)
        serializer = StudentWordSerializer(student_words, many=True)
        return Response(serializer.data)


class StudentWordListByWord(APIView):
    """
    List all student words by word id.
    """
    def get(self, request, pk):
        student_words = StudentWord.objects.filter(word=pk)
        serializer = StudentWordSerializer(student_words, many=True)
        return Response(serializer.data)


class StudentWordListByStudentAndWord(APIView):
    """
    List all student words by student id and word id.
    """
    def get(self, request, student_pk, word_pk):
        student_words = StudentWord.objects.filter(student=student_pk, word=word_pk)
        serializer = StudentWordSerializer(student_words, many=True)
        return Response(serializer.data)


class Get10RandomWords(APIView):
    """
    Get 10 random words for specified student that have not been in StudentWord table.
    """
    def get(self, request, chat_id):
        try:
            student = Student.objects.get(chat_id=chat_id)
        except Student.DoesNotExist:
            return Response(
                {'error': 'Student not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        student_words = StudentWord.objects.filter(student=student)
        words = Word.objects.exclude(id__in=student_words.values('word'))
        if len(words) >= 10:
            random_words = random.sample(list(words), 10)
        else:
            random_words = random.sample(list(words), len(words))
        for word in random_words:
            StudentWord.objects.create(student=student, word=word)

        serializer = WordSerializer(random_words, many=True)
        return Response(serializer.data)


class CheckAnswer(APIView):
    """
    Check student answer and return correct answer.
    """
    def post(self, request):
        try:
            student = Student.objects.get(chat_id=request.data['chat_id'])
        except Student.DoesNotExist:
            return Response(
                {'error': 'Student not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            word = Word.objects.get(id=request.data['word_id'])
        except Word.DoesNotExist:
            return Response(
                {'error': 'Word not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            student_word = StudentWord.objects.get(student=student, word=word)
        except StudentWord.DoesNotExist:
            return Response(
                {'error': 'Student word not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        if student_word.word.name == request.data['answer']:
            return Response(
                {'correct': True},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'correct': False, 'answer': student_word.word.name},
                status=status.HTTP_200_OK
            )
        

from rest_framework.serializers import ModelSerializer

from .models import (
    Word, Topic,
    Student, StudentWord
)


class TopicSerializer(ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'


class WordSerializer(ModelSerializer):

    class Meta:
        model = Word
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'


class StudentWordSerializer(ModelSerializer):
        
    class Meta:
        model = StudentWord
        fields = '__all__'

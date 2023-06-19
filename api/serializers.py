from rest_framework.serializers import ModelSerializer

from .models import (
    Word, Topic,
    Student, StudentWord,
    WordImage, TopicImage,
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


class WordImageSerializer(ModelSerializer):

    class Meta:
        model = WordImage
        fields = '__all__'


class TopicImageSerializer(ModelSerializer):

    class Meta:
        model = TopicImage
        fields = '__all__'

from django.urls import path

from .views import (
    TopicList, TopicDetail,
    WordList, WordDetail,
    StudentList, StudentDetail,
    StudentWordList, StudentWordDetail,
    StudentWordListByStudent, StudentWordListByWord, StudentWordListByStudentAndWord,
    Get10RandomWords,
    CheckAnswer,
    GetRandomWordImage,
)


urlpatterns = [
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('word/', WordList.as_view()),
    path('topic/', TopicList.as_view()),
    path('word/<int:pk>/', WordList.as_view()),
    path('student/<int:pk>/words/', WordList.as_view()),
    path('random-word/<int:chat_id>/', Get10RandomWords.as_view()),
    path('check-word/', CheckAnswer.as_view()),
    path('random-word-image/<int:chat_id>/<int:word_id>/', GetRandomWordImage.as_view()),
]

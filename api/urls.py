from django.urls import path

from .views import TopicView, WordView, StudentView, StudentWordView, GetRandomWordView, CheckAnswerView

urlpatterns = [
    path('topics/', TopicView.as_view()),
    path('topics/<int:pk>/', TopicView.as_view()),
    path('words/', WordView.as_view()),
    path('words/<int:pk>/', WordView.as_view()),
    path('students/', StudentView.as_view()),
    path('students/<int:pk>/', StudentView.as_view()),
    path('studentwords/', StudentWordView.as_view()),
    path('studentwords/<int:pk>/', StudentWordView.as_view()),
    path('get_random_word/<int:chat_id>/', GetRandomWordView.as_view()),
    path('check_answer/<int:chat_id>/<int:word_id>/<answer>/', CheckAnswerView.as_view()),
]

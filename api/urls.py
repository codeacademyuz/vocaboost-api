from django.urls import path

from .views import TopicView, WordView, StudentView, StudentWordView

urlpatterns = [
    path('topics/', TopicView.as_view()),
    path('topics/<int:pk>/', TopicView.as_view()),
    path('words/', WordView.as_view()),
    path('words/<int:pk>/', WordView.as_view()),
    path('students/', StudentView.as_view()),
    path('students/<int:pk>/', StudentView.as_view()),
    path('studentwords/', StudentWordView.as_view()),
    path('studentwords/<int:pk>/', StudentWordView.as_view()),
]

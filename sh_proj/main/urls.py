from django.urls import path
from . import views
from .views import LessonView

urlpatterns = [
    path('', views.main_render, name='lesson_list'),
    path('schedule/', LessonView.as_view(), name='schedule'),
]

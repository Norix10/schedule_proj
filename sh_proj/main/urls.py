from django.urls import path
from . import views
from .views import LessonView

urlpatterns = [
    path('', views.group_render, name='group_list'),
    path('schedule/<str:group_name>/', views.group_schedule, name='group_schedule'),
    path('json/', LessonView.as_view(), name='schedule'),
]

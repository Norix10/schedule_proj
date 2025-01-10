from django.shortcuts import render
from .models import Lesson
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import LessonSerializer
# Create your views here.

def main_render(request):
    lessons = Lesson.objects.all().order_by('day__day_of_week', 'time')
    grouped_lessons = {}
    for lesson in lessons:
        day_of_week = lesson.day.get_day_of_week_display()
        if day_of_week not in grouped_lessons:
            grouped_lessons[day_of_week] = []
        grouped_lessons[day_of_week].append(lesson)

    return render(request, 'main/main.html', {'grouped_lessons': grouped_lessons})


class LessonView(APIView):
    def get(self, request):
        day = request.query_params.get('day', None)
        if day:
            lessons = Lesson.objects.filter(day__day_of_week=day).order_by('day__day_of_week', 'time')
        else:
            lessons = Lesson.objects.all().order_by('day__day_of_week', 'time')
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

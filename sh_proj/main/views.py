from django.shortcuts import render, get_object_or_404
from .models import Lesson, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import LessonSerializer
# Create your views here.

def group_render(request):
    groups = Group.objects.all()
    return render(request, 'main/welcome.html', {'groups': groups})

def group_schedule(request, group_name):
    group = get_object_or_404(Group, group_name=group_name)
    lessons = Lesson.objects.filter(group=group).order_by('day__day_of_week', 'time')
    grouped_lessons = {}
    for lesson in lessons:
        day_of_week = lesson.day.get_day_of_week_display()
        if day_of_week not in grouped_lessons:
            grouped_lessons[day_of_week] = []
        grouped_lessons[day_of_week].append(lesson)

    ordered_days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П’ятниця', 'Субота', 'Неділя']
    grouped_lessons = {day: grouped_lessons.get(day, []) for day in ordered_days}

    return render(request, 'main/main.html', {'grouped_lessons': grouped_lessons, 'group_name': group_name})

class LessonView(APIView):
    def get(self, request):
        day = request.query_params.get('day', None)
        if day:
            lessons = Lesson.objects.filter(day__day_of_week=day).order_by('day__day_of_week', 'time')
        else:
            lessons = Lesson.objects.all().order_by('day__day_of_week', 'time')
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
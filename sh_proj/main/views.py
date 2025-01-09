from django.shortcuts import render
from .models import Lesson
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import LessonSerializer
# Create your views here.

def main_render(request):
    lessons = Lesson.objects.all().order_by('day_of_week', 'time')
    return render(request, 'main/main.html', {'lessons': lessons})

class LessonView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

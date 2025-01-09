from django.template.defaultfilters import first
from rest_framework import serializers
from .models import Lesson


#class LessonSerializer(serializers.ModelSerializer):
   # first_name = serializers.CharField(source='teacher.first_name')
   # middle_name = serializers.CharField(source='teacher.middle_name')
   # last_name = serializers.CharField(source='teacher.last_name')
   # full_name = first_name + middle_name + last_name

   # class Meta:
   #     model = Lesson
   #     fields = ("id", "day_of_week", "time", "subject",
   #               "room", "full_name")

class LessonSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ("id", "day_of_week", "time", "subject", "room", "full_name")

    def get_full_name(self, obj):
        if obj.teacher:
            return f"{obj.teacher.first_name} {obj.teacher.middle_name} {obj.teacher.last_name}".strip()
        return ""
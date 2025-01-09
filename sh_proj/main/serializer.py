from django.template.defaultfilters import first
from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    room_s = serializers.SerializerMethodField()
    class Meta:
        model = Lesson
        fields = ("id", "day_of_week", "time", "subject", "room_s", "full_name")

    def get_full_name(self, obj):
        if obj.teacher:
            return f"{obj.teacher.first_name} {obj.teacher.middle_name} {obj.teacher.last_name}".strip()
        return ""

    def get_room_s(self, obj):
        if obj.room:
            return f"{obj.room.room_name} {obj.room.room_number}".strip()
        return ""
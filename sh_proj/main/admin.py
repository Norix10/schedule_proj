from django.contrib import admin
from .models import Lesson, Teacher, Room


admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Room)
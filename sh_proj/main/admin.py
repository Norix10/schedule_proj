from django.contrib import admin
from .models import Lesson, Teacher, Room, Day


admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Day)
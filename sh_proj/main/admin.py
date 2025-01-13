from django.contrib import admin
from .models import Lesson, Teacher, Room, Group, Day

admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Day)

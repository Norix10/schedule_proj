from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    room_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.room_name} {self.room_number}"

class Day(models.Model):
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ('Monday', 'Понеділок'),
            ('Tuesday', 'Вівторок'),
            ('Wednesday', 'Середа'),
            ('Thursday', 'Четвер'),
            ('Friday', 'П’ятниця'),
            ('Saturday', 'Субота'),
        ],
        unique=True
    )

    def __str__(self):
        return f"{self.get_day_of_week_display()}"

class Lesson(models.Model):
    time = models.TimeField()
    subject = models.CharField(max_length=100)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='lessons', default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teach')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='teach')

    def __str__(self):
        return f"{self.subject} ({self.day.get_day_of_week_display()}, {self.time})"

# Generated by Django 5.1.4 on 2025-01-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_room_alter_lesson_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(default=0),
        ),
    ]

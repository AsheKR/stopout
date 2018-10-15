from django.db import models


class School(models.Model):
    school_name = models.CharField(max_length=80)


class Student(models.Model):
    student_name = models.CharField(max_length=80)
    now_school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    best_friend = models.ManyToManyField(
        'self',
        on_delete=models.CASCADE,
    )

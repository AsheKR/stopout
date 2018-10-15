from django.db import models


class School(models.Model):
    school_name = models.CharField(max_length=80)

    def __str__(self):
        return self.school_name


class Student(models.Model):
    student_name = models.CharField(max_length=80)
    now_school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    best_friend = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.student_name

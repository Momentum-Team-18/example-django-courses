from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

CONSTANT = "Exists and can be used anywhere in the subsequent code"


class User(AbstractUser):
    TEACHER = 'TE'
    STUDENT = 'ST'

    USER_TYPE_CHOICES = [
        (TEACHER, "Teacher"),
        (STUDENT, "Student"),
    ]
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    type = models.CharField(
        max_length=50, choices=USER_TYPE_CHOICES, default=STUDENT)


class Course(models.Model):
    MONDAY = 'M'
    TUESDAY = "T"
    WEDNESDAY = 'W'
    THURSDAY = 'TH'

    DAY_CHOICES = [
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
    ]
    title = models.CharField(max_length=100)
    day = models.CharField(max_length=50, choices=DAY_CHOICES)
    start_time = models.TimeField()
    length_in_hours = models.FloatField(default=1.00)
    teacher = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

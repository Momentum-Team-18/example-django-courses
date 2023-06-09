# Generated by Django 4.2.1 on 2023-06-01 14:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_students_alter_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_taking', to=settings.AUTH_USER_MODEL),
        ),
    ]

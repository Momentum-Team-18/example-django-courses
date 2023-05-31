# Generated by Django 4.2.1 on 2023-05-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('TE', 'Teacher'), ('ST', 'Student')], default='ST', max_length=50),
        ),
    ]
from django.db import models
from django.contrib.auth.models import User, Group

class Subject(models.Model):
    subjectName = models.CharField(max_length=30)
    teacherAccount = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subjects')
    targetGroup = models.ManyToManyField(Group, related_name='subjects')  # Link to user groups

    def __str__(self):
        return self.subjectName

class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='homeworks')  # Link to Subject
    title = models.CharField(max_length=300)  # Example: "Read the short story 'LLL' of Mmm"
    description = models.CharField(max_length=500, blank=True)  # Example: "Be prepared to read it in class"
    dueDate = models.DateField()  # Example: Due 10-10-2025
    attachedFile = models.FileField(upload_to='uploads/homeworkRelated/', blank=True)  # Example: LLL by Mmm.pdf

    def __str__(self):
        return self.title



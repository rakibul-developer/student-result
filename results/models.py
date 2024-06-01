from django.db import models

# Create your models here.

# Student Model
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField(unique=True)
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Subject Model 
class Subject(models.Model):
    name=models.CharField(max_length=100)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    
# Exam Model 
class Exam(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.name

# Result Model 
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.subject.name} - ({self.exam.name})'

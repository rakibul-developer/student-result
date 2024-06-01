from django import forms
from .models import *

# Student Form 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

# Subject Form 
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code']

# Exam Form 
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'date']

# Result Form 
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'subject', 'exam', 'marks']

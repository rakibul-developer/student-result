from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# All student list 
@login_required(login_url='search_result')
def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    
    return render(request, 'results/student_list.html', context)

# Create a new student
@login_required(login_url='search_result')
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully.')
            return redirect('student_list')
        else:
            messages.error(request, 'Student creation failed.') 
            return render(request, 'results/student_form.html', {'form': form})
    else:
        form = StudentForm()
        context = {'form': form}
        return render(request, 'results/student_form.html', context)

# Update a student 
@login_required(login_url='search_result')
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('student_list')
        else:
            messages.error(request, 'Student update failed.')
            return render(request, 'results/student_form.html', {'form': form})
    else:
        form = StudentForm(instance=student)
        context = {'form': form}
        return render(request, 'results/student_form.html', context)

# Delete a student 
@login_required(login_url='search_result')
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('student_list')
    else:
        context = {'student': student}
        return render(request, 'results/student_confirm_delete.html', context)
    
# Search for student information
def search_result(request):
    query = request.GET.get('q')
    student = None
    results = None
    if query:
        student = Student.objects.filter(roll=query).first()
        if student:
            results = Result.objects.filter(student=student)
    return render(request, 'results/search_result.html', {'student': student, 'results': results, 'query': query})

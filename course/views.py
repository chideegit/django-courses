from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Course
from .form import * 

def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.author = request.user
            var.save()
            messages.success(request, 'Course added and saved to Database')
            return redirect('all-courses')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('add-course')
    else:
        form = AddCourseForm()
        context = {'form':form}
    return render(request, 'course/add_course.html', context)

def update_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course information is now updated and saved')
            return redirect('all-courses')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('all-courses')
    else:
        form = UpdateCourseForm(instance=course)
        context = {'form':form}
    return render(request, 'course/update_course.html', context)

def all_courses(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'course/all-courses.html', context)

def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    messages.success(request, 'Course has been deleted')
    return redirect('all-courses')

def enrol_course(request, pk):
    course = Course.objects.get(pk=pk)
    EnrolCourse.objects.create(
        user = request.user, 
        course = course
    )
    messages.success(request, 'You have successfully enrolled for this course')
    return redirect('dashboard')

def all_enrolled_courses(request):
    courses = EnrolCourse.objects.filter(user=request.user)
    context = {'courses':courses}
    return render(request, 'course/all_enrolled_courses.html', context)



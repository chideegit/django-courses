from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Course
from .form import * 
from django.urls import reverse

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

def course_details(request, pk):
    course = Course.objects.get(pk=pk)
    if course.enrolcourse_set.filter(course=course, user=request.user).exists():
        check = True
    else:
        check = False
    context = {'course':course, 'check':check}
    return render(request, 'course/course_details.html', context)

def all_courses(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'course/all_courses.html', context)

def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    messages.success(request, 'Course has been deleted')
    return redirect('all-courses')

def enrol_course(request, pk):
    course = Course.objects.get(pk=pk)
    if not EnrolCourse.objects.filter(course=course, user=request.user).exists():
        EnrolCourse.objects.create(
            user = request.user, 
            course = course, 
            is_enrolled = True
        )
        messages.success(request, 'You have successfully enrolled for this course')
        return HttpResponseRedirect(reverse('course-details', args=[course.pk]))
    else:
        messages.warning(request, 'You are already enrolled for this course')
        
        return redirect('dashboard')

def all_enrolled_courses(request):
    courses = EnrolCourse.objects.filter(user=request.user)
    context = {'courses':courses}
    return render(request, 'course/all_enrolled_courses.html', context)

def save_course(request, pk):
    course = Course.objects.get(pk=pk)
    if not SaveCourse.objects.filter(course=course, user=request.user).exists():
        SaveCourse.objects.create(course=course, user=request.user)
        messages.success(request, 'Course has been saved to your profile')
        return redirect('dashboard')
    else:
        messages.warning(request, 'Course has already been saved')
        return redirect('dashboard')



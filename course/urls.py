from django.urls import path 
from .views import *

urlpatterns = [
    path('add-course/', add_course, name='add-course'), 
    path('update-course/<int:pk>/', update_course, name='update-course'), 
    path('all-courses/', all_courses, name='all-courses'), 
    path('delete-course/<int:pk>/', delete_course, name='delete-course'), 
    path('course-details/<int:pk>/', course_details, name='course-details'), 
    path('enrol-course/<int:pk>/', enrol_course, name='enrol-course'), 
    path('all-enrolled-courses/', all_enrolled_courses, name='all-enrolled-courses'), 
    path('save-course/<int:pk>/', save_course, name='save-course')
]
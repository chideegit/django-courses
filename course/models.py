from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title 
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_link = models.URLField(null=True)
    article_link = models.URLField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class EnrolCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_enrolled = models.BooleanField(default=False)

class SaveCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
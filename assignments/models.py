from django.db import models

# Create your models here.
from django.db import models
from courses.models import Course
from users.models import CustomUser

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='submissions')
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.username}"
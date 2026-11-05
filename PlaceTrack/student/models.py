from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    registration_no = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    image = models.ImageField(upload_to="student_images/")
    address = models.TextField()

    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, blank=True, null=True)
    semester = models.IntegerField()
    cgpa = models.DecimalField()
    backlog = models.IntegerField(default=0)

    skill = models.TextField()
    projects = models.TextField(blank=True, null=True)
    expirience = models.TextField(blank=True, null=True)

    resume = models.FileField(upload_to="resumes/")
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)

    job_role = models.CharField(max_length=200)
    job_location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):
    post_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    name_company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    skills = models.ManyToManyField('Skill', related_name='jobs', blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    required_level = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    full_name = models.CharField(max_length=255)
    summary = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    skills = models.ManyToManyField(Skill, related_name='resumes', blank='True')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}'s Resume"
    
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.job.title} by {self.resume.user.username}"

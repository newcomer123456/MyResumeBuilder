from django.contrib import admin
from .models import Job, Skill, Resume

# Register your models here.
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Resume)
from django.shortcuts import render
from .models import Job, Skill, Resume
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View 
from .forms import JobForm, JobUpdateForm, ResumeForm, ResumeUpdateForm
from django.urls import reverse_lazy

# Create your views here.
class JobCreateView(CreateView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'main_app/job_create.html'
    form_class = JobForm
    success_url = reverse_lazy('jobs-list')
     
class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'main_app/jobs_list.html'

class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'main_app/job_detail.html'

class JobUpdateView(UpdateView):
    model = Job
    context_object_name = 'job'
    template_name = 'main_app/job_update.html'
    form_class = JobUpdateForm
    success_url = reverse_lazy('jobs-list')

class JobDeleteView(DeleteView):
    model = Job
    context_object_name = 'job'
    template_name = 'main_app/job_delete.html'
    success_url = reverse_lazy('jobs-list')





class ResumeCreateView(CreateView):
    model = Resume
    context_object_name = 'resumes'
    template_name = 'main_app/resume_create.html'
    form_class = ResumeForm
    success_url = reverse_lazy('resumes-list')
    
class ResumeListView(ListView):
    model = Resume
    context_object_name = 'resumes'
    template_name = 'main_app/resumes_list.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class ResumeDetailView(DetailView):
    model = Resume
    context_object_name = 'resume'
    template_name = 'main_app/resume_detail.html'

class ResumeUpdateView(UpdateView):
    model = Resume
    context_object_name = 'resume'
    template_name = 'main_app/resume_update.html'
    form_class = ResumeUpdateForm
    success_url = reverse_lazy('resumes-list')

class ResumeDeleteView(DeleteView):
    model = Resume
    context_object_name = 'resume'
    template_name = 'main_app/resume_delete.html'
    success_url = reverse_lazy('resumes-list')





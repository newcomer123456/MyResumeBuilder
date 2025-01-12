from django.urls import path
from main_app import views

urlpatterns = [
    path('jobs/', views.JobListView.as_view(), name='jobs-list'),
    path('jobs/create/', views.JobCreateView.as_view(), name='create-job'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='detail-job'),
    path('jobs/<int:pk>/update/', views.JobUpdateView.as_view(), name='update-job'),
    path('jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='delete-job'),
    path('resumes/', views.ResumeListView.as_view(), name='resumes-list'),
    path('resumes/create/', views.ResumeCreateView.as_view(), name='create-resume'),
    path('resumes/<int:pk>/', views.ResumeDetailView.as_view(), name='detail-resume'),
    path('resumes/<int:pk>/update/', views.ResumeUpdateView.as_view(), name='update-resume'),
    path('resumes/<int:pk>/delete/', views.ResumeDeleteView.as_view(), name='delete-resume'),
]
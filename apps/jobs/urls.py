from django.urls import path
from .views import JobListCreateView, JobDetailView, RecruiterJobsView

urlpatterns = [
    path('',          JobListCreateView.as_view(), name='job-list-create'),
    path('/', JobDetailView.as_view(),     name='job-detail'),
    path('my-jobs/',  RecruiterJobsView.as_view(), name='my-jobs'),
]
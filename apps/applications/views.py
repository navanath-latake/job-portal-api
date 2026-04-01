from rest_framework import generics, permissions
from .models import Application
from .serializers import ApplicationSerializer, ApplicationStatusSerializer
from apps.accounts.permissions import IsApplicant, IsRecruiter
from apps.jobs.models import Job
from rest_framework.exceptions import PermissionDenied


class ApplyView(generics.CreateAPIView):
    serializer_class   = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]


class MyApplicationsView(generics.ListAPIView):
    serializer_class   = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user
        ).select_related('job', 'applicant').order_by('-created_at')


class JobApplicationsView(generics.ListAPIView):
    serializer_class   = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        try:
            job = Job.objects.get(pk=job_id, recruiter=self.request.user)
        except Job.DoesNotExist:
            raise PermissionDenied('You do not own this job listing.')
        return Application.objects.filter(
            job=job
        ).select_related('applicant', 'job').order_by('-created_at')


class ApplicationStatusView(generics.UpdateAPIView):
    serializer_class   = ApplicationStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    http_method_names  = ['patch']

    def get_queryset(self):
        return Application.objects.filter(
            job__recruiter=self.request.user
        ).select_related('job')